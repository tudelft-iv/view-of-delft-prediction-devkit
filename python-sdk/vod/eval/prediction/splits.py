# View-of-Delft Prediction dev-kit, based on the nuScenes dev-kit.
# Code written by Freddy Boulton.

import json
import os
from itertools import chain
from typing import List

from vod.utils.splits import create_splits_scenes


def get_prediction_challenge_split(
    split: str, dataroot: str = "/data/sets/vod"
) -> List[str]:
    """
    Gets a list of {instance_token}_{sample_token} strings for each split.
    :param split: One of 'mini_train', 'mini_val', 'train', 'val'.
    :param dataroot: Path to the VOD dataset.
    :return: List of tokens belonging to the split. Format {instance_token}_{sample_token}.
    """
    if split not in {"mini_train", "mini_val", "train", "train_val", "val"}:
        raise ValueError(
            "split must be one of (mini_train, mini_val, train, train_val, val)"
        )

    if split == "train_val":
        split_name = "train"
    else:
        split_name = split

    if split == "train_val" or split == "train" or split == "val":
        dirname = "v1.0-trainval"
    else:
        dirname = f"v1.0-{split}"

    path_to_file = os.path.join(dataroot, dirname, "prediction_scenes.json")
    prediction_scenes = json.load(open(path_to_file, "r"))
    scenes = create_splits_scenes()
    scenes_for_split = scenes[split_name]

    token_list_for_scenes = map(
        lambda scene: prediction_scenes.get(scene, []), scenes_for_split
    )

    return list(chain.from_iterable(token_list_for_scenes))
