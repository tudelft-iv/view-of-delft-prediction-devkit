# View-of-Delft Prediction dev-kit, based on the nuScenes dev-kit.
# Code written by Holger Caesar, 2018.

from typing import Dict, List

from vod import VOD

train = [
    "q4hez5edjjtfph90o7y22t1tdgnnqfkp",
    "8k2fk99l0phbz83lxtc25q87e06jarnk",
    "owogq5dslsmf48dagon6fxeb108ts8eh",
    "8ljts8qndgju0bcdh3ldez8y34jl50u8",
    "xfoiw0w00ggr42lp2mwt7sanxjm9wtuy",
    "okwsl2921sjnw8t017nb0aq6y9k29w8r",
    "0mlrodqf39vvdidiifyvlw313rnahyht",
    "mkr529kg3p45sk0jgrjd8szfegwfot79",
    "mypp0mldnv4kenlr3gqt8638qv9f7pkk",
    "7kjhncjj4m5883qwu0rjo1j62hu8hdx8",
    "f7b4df1owz80izwy51roqruva31ssmqn",
    "87cgygi3l41q3ft0ct9dizxclqg4b434",
]

val = [
    "smsz20lamf98gmpt1ppia0oefubih4kw",
    "63p8qt0d4biowur5es45sojf7fj3h5iu",
    "9q5jy0dlaz7blaw6fd1fizdnnw2dl4to",
    "0j93nt1dpgzxvhppg9smwlul7ka75rb4",
]

test = [
    "r4bf59dp37h696i9gg03siw2gq8p4msn",
    "k3rblq6f3tulyggqfyjz8st4ewokv8fa",
    "79fxw6jjbwgw8lax0ukcwtrujv4ktj5v",
    "4tym7cobttc56enha5uepsyi3xhtmpgy",
    "bnqhhjrb8zn6frz29emtekjk7qwo3q3p",
    "2vrb1jiswk9ocphpj1fzouby4d2f9cow",
    "wvbc8v977mciwp2b7qyxerv0xyw6sr60",
]

mini_train = [
    "q4hez5edjjtfph90o7y22t1tdgnnqfkp",
    "8k2fk99l0phbz83lxtc25q87e06jarnk",
    "owogq5dslsmf48dagon6fxeb108ts8eh",
]

mini_val = [
    "smsz20lamf98gmpt1ppia0oefubih4kw",
    "63p8qt0d4biowur5es45sojf7fj3h5iu",
]


def create_splits_logs(split: str, vod_: VOD) -> List[str]:
    """
    Returns the logs in each dataset split of VOD.
    Note: Previously this script included the teaser dataset splits. Since new scenes from those logs were added and
          others removed in the full dataset, that code is incompatible and was removed.
    :param split: VOD split.
    :param vod_: VOD instance.
    :return: A list of logs in that split.
    """
    # Load splits on a scene-level.
    scene_splits = create_splits_scenes(verbose=False)

    assert (
        split in scene_splits.keys()
    ), "Requested split {} which is not a known VOD split.".format(split)

    # Check compatibility of split with vod_.version.
    version = vod_.version
    if split in {"train", "val"}:
        assert version.endswith(
            "trainval"
        ), "Requested split {} which is not compatible with VOD version {}".format(
            split, version
        )
    elif split in {"mini_train", "mini_val"}:
        assert version.endswith(
            "mini"
        ), "Requested split {} which is not compatible with VOD version {}".format(
            split, version
        )
    elif split == "test":
        assert version.endswith(
            "test"
        ), "Requested split {} which is not compatible with VOD version {}".format(
            split, version
        )
    else:
        raise ValueError(
            "Requested split {} which this function cannot map to logs.".format(split)
        )

    # Get logs for this split.
    scene_to_log = {
        scene["name"]: vod_.get("log", scene["log_token"])["logfile"]
        for scene in vod_.scene
    }
    logs = set()
    scenes = scene_splits[split]
    for scene in scenes:
        logs.add(scene_to_log[scene])

    return list(logs)


def create_splits_scenes(verbose: bool = False) -> Dict[str, List[str]]:
    """
    Similar to create_splits_logs, but returns a mapping from split to scene names, rather than log names.
    The splits are as follows:
    - train/val/test: The standard splits of the VoD dataset (12/4/7 scenes).
    - mini_train/mini_val: Train and val splits of the mini subset used for visualization and debugging (4/2 scenes).
    :param verbose: Whether to print out statistics on a scene level.
    :return: A mapping from split name to a list of scenes names in that split.
    """
    # Use hard-coded splits.
    all_scenes = train + val + test
    NUM_SCENES = 23
    assert (
        len(all_scenes) == NUM_SCENES and len(set(all_scenes)) == NUM_SCENES
    ), "Error: Splits incomplete!"
    scene_splits = {
        "train": train,
        "val": val,
        "test": test,
        "mini_train": mini_train,
        "mini_val": mini_val,
    }

    # Optional: Print scene-level stats.
    if verbose:
        for split, scenes in scene_splits.items():
            print("%s: %d" % (split, len(scenes)))
            print("%s" % scenes)

    return scene_splits


if __name__ == "__main__":
    # Print the scene-level stats.
    create_splits_scenes(verbose=True)
