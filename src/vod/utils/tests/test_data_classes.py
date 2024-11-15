# View-of-Delft Prediction dev-kit, based on the nuScenes dev-kit.
# Code written by Holger Caesar, 2021.

import os
import unittest

from vod import VOD
from vod.utils.data_classes import LidarPointCloud, RadarPointCloud


class TestDataClasses(unittest.TestCase):

    def test_load_pointclouds(self):
        """
        Loads up lidar and radar pointclouds.
        """
        assert 'VOD' in os.environ, 'Set VOD env. variable to enable tests.'
        dataroot = os.environ['VOD']
        vod_ = VOD(version='v1.0-mini', dataroot=dataroot, verbose=False)
        sample_rec = vod_.sample[0]
        lidar_name = vod_.get('sample_data', sample_rec['data']['LIDAR_TOP'])['filename']
        radar_name = vod_.get('sample_data', sample_rec['data']['RADAR_FRONT'])['filename']
        lidar_path = os.path.join(dataroot, lidar_name)
        radar_path = os.path.join(dataroot, radar_name)
        pc1 = LidarPointCloud.from_file(lidar_path)
        pc2 = RadarPointCloud.from_file(radar_path)
        pc3, _ = LidarPointCloud.from_file_multisweep(vod_, sample_rec, 'LIDAR_TOP', 'LIDAR_TOP', nsweeps=2)
        pc4, _ = RadarPointCloud.from_file_multisweep(vod_, sample_rec, 'RADAR_FRONT', 'RADAR_FRONT', nsweeps=2)

        # Check for valid dimensions.
        assert pc1.points.shape[0] == pc3.points.shape[0] == 4, 'Error: Invalid dimension for lidar pointcloud!'
        assert pc2.points.shape[0] == pc4.points.shape[0] == 18, 'Error: Invalid dimension for radar pointcloud!'
        assert pc1.points.dtype == pc3.points.dtype, 'Error: Invalid dtype for lidar pointcloud!'
        assert pc2.points.dtype == pc4.points.dtype, 'Error: Invalid dtype for radar pointcloud!'


if __name__ == '__main__':
    unittest.main()
