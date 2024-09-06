# View-of-Delft Prediction dev-kit, based on the nuScenes dev-kit.
# Modified by Hidde Boekema, 2024.
# TODO describe modifications.

import math
from typing import Any, Dict, List, Tuple

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import BSpline, splev

# (x, y, yaw) in global frame
Pose = Tuple[float, float, float]

SplinePath = Tuple[List[float], List[float], int]


def make_spline_from_record(spline_path: SplinePath):
    knots, coeff, order = spline_path
    assert type(order) == int
    return BSpline(np.array(knots), np.array(coeff), order)


def principal_value(angle_in_radians: float) -> float:
    """
    Ensures the angle is within [-pi, pi).
    :param angle_in_radians: Angle in radians.
    :return: Scaled angle in radians.
    """

    interval_min = -math.pi
    two_pi = 2 * math.pi
    scaled_angle = (angle_in_radians - interval_min) % two_pi + interval_min
    return scaled_angle


def get_transformation_at_step(pose: Pose, step: float) -> Pose:
    """
    Get the affine transformation at s meters along the path.
    :param pose: Pose represented as tuple (x, y, yaw).
    :param step: Length along the arcline path in range (0, length_of_arcline_path].
    :return: Transformation represented as pose tuple.
    """

    theta = pose[2] * step
    ctheta = math.cos(theta)
    stheta = math.sin(theta)

    if abs(pose[2]) < 1e-6:
        return pose[0] * step, pose[1] * step, theta
    else:
        new_x = (pose[1] * (ctheta - 1.0) + pose[0] * stheta) / pose[2]
        new_y = (pose[0] * (1.0 - ctheta) + pose[1] * stheta) / pose[2]
        return new_x, new_y, theta


def apply_affine_transformation(pose: Pose, transformation: Pose) -> Pose:
    """
    Apply affine transformation to pose.
    :param pose: Starting pose.
    :param transformation: Affine transformation represented as a pose tuple.
    :return: Pose tuple - the result of applying the transformation to the starting pose.
    """

    new_x = (
        math.cos(pose[2]) * transformation[0]
        - math.sin(pose[2]) * transformation[1]
        + pose[0]
    )
    new_y = (
        math.sin(pose[2]) * transformation[0]
        + math.cos(pose[2]) * transformation[1]
        + pose[1]
    )
    new_yaw = principal_value(pose[2] + transformation[2])

    return new_x, new_y, new_yaw


def _get_lie_algebra(
    segment_sign: Tuple[int, int, int], radius: float
) -> List[Tuple[float, float, float]]:
    """
    Gets the Lie algebra for an arcline path.
    :param segment_sign: Tuple of signs for each segment in the arcline path.
    :param radius: Radius of curvature of the arcline path.
    :return: List of lie algebra poses.
    """

    return [
        (1.0, 0.0, segment_sign[0] / radius),
        (1.0, 0.0, segment_sign[1] / radius),
        (1.0, 0.0, segment_sign[2] / radius),
    ]


def pose_at_length(spline_path: SplinePath, pos: float) -> Tuple[float, float, float]:
    """
    Retrieves pose at l meters along the spline path.
    :param spline_path: SplinePath object.
    :param pos: Get the pose this many meters along the path.
    :return: Pose tuple.
    """

    raise NotImplementedError


def angle_between_vectors(v1, v2):
    angle_radians = np.arctan2(v2[1], v2[0]) - np.arctan2(v1[1], v1[0])
    return angle_radians


def tangent_length(spline: BSpline, u: float):
    x_deriv, y_deriv = splev(u, spline, 1)
    return np.sqrt(x_deriv ** 2 + y_deriv ** 2)


def spline_length(spline: BSpline):
    length, err = quad(
        lambda u: tangent_length(spline, u), 0, 1, epsabs=1e-5, epsrel=1e-5, limit=1000
    )
    return length


def discretize_spline(
    spline: BSpline, resolution_meters: float
) -> List[Tuple[int, int]]:
    length = spline_length(spline)

    num_pts = length // resolution_meters
    remainder = length % resolution_meters
    remainder_frac = remainder / length

    t = np.linspace(0, 1 - remainder_frac, int(num_pts) + 1)

    # add spline endpoint
    t = np.hstack((t, [1.0]))
    # t = np.linspace(0, 1, 40)

    spline_pts = np.stack(spline(t), axis=0)
    # dists = [np.linalg.norm(p2 - p1) for p1, p2 in zip(spline_pts[:-1], spline_pts[1:])]
    # print(dists)
    return spline_pts


def discretize(spline_path: SplinePath, resolution_meters: float) -> List[Pose]:
    """
    Discretize a spline path.
    :param spline_path: SplinePath record.
    :param resolution_meters: How finely to discretize the path.
    :return: List of pose tuples.
    """
    spline = make_spline_from_record(spline_path)
    xy = discretize_spline(spline, resolution_meters)

    yaws = []
    for p1, p2 in zip(xy[:-1], xy[1:]):
        p12 = p2 - p1
        yaw = np.arctan2(p12[1], p12[0])
        # yaw = 0
        yaws.append([yaw])
    yaws.append(yaws[-1])
    discretization = np.concatenate([xy, yaws], axis=-1)
    # yaws = np.zeros((len(xy), 1))
    # discretization = np.concatenate([xy, np.zeros((len(xy), 1))], axis=-1)

    return discretization


def discretize_lane(lane: SplinePath, resolution_meters: float) -> List[Pose]:
    """
    Discretizes a lane and returns list of all the poses alone the lane.
    :param lane: Lanes are represented by the centerline.
    :param resolution_meters: How finely to discretize the lane. Smaller values ensure curved
        lanes are properly represented.
    :return: List of pose tuples along the lane.
    Basically an alias for discretize() to maintain the original nuScenes interface.
    """
    poses = discretize(lane, resolution_meters)
    return poses


def length_of_lane(lane: SplinePath) -> float:
    """
    Calculates the length of a lane in meters.
    :param lane: Lane.
    :return: Length of lane in meters.
    """

    spline = make_spline_from_record(lane)
    return spline_length(spline)


def project_pose_to_lane(
    pose: Pose, lane: List[SplinePath], resolution_meters: float = 0.5
) -> Tuple[Pose, float]:
    """
    Find the closest pose on a lane to a query pose and additionally return the
    distance along the lane for this pose. Note that this function does
    not take the heading of the query pose into account.
    :param pose: Query pose.
    :param lane: Will find the closest pose on this lane.
    :param resolution_meters: How finely to discretize the lane.
    :return: Tuple of the closest pose and the distance along the lane
    """

    discretized_lane = discretize_lane(lane, resolution_meters=resolution_meters)

    xy_points = np.array(discretized_lane)[:, :2]
    closest_pose_index = np.linalg.norm(xy_points - pose[:2], axis=1).argmin()

    closest_pose = discretized_lane[closest_pose_index]
    distance_along_lane = closest_pose_index * resolution_meters
    return closest_pose, distance_along_lane


def _find_index(distance_along_lane: float, lengths: List[float]) -> int:
    """
    Helper function for finding of path along lane corresponding to the distance_along_lane.
    :param distance_along_lane: Distance along the lane (in meters).
    :param lengths: Cumulative distance at each end point along the paths in the lane.
    :return: Index of path.
    """

    if len(lengths) == 1:
        return 0
    else:
        return min(
            index
            for index, length in enumerate(lengths)
            if distance_along_lane <= length
        )


def get_curvature_at_distance_along_lane(
    distance_along_lane: float, lane: List[SplinePath]
) -> float:
    """
    Computes the unsigned curvature (1 / meters) at a distance along a lane.
    :param distance_along_lane: Distance along the lane to calculate the curvature at.
    :param lane: Lane to query.
    :return: Curvature, always non negative.
    """

    # total_length_at_segments = np.cumsum([sum(path["segment_length"]) for path in lane])
    # segment_index = _find_index(distance_along_lane, total_length_at_segments)

    # path = lane[segment_index]
    # path_length = path["segment_length"]

    # if segment_index > 0:
    #     distance_along_path = (
    #         distance_along_lane - total_length_at_segments[segment_index - 1]
    #     )
    # else:
    #     distance_along_path = distance_along_lane

    # segment_index = _find_index(distance_along_path, np.cumsum(path_length))

    # segment_shape = path["shape"][segment_index]

    # # Straight lanes have no curvature
    # if segment_shape == "S":
    #     return 0
    # else:
    #     return 1 / path["radius"]
    raise NotImplementedError
