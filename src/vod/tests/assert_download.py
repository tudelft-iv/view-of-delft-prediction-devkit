# View-of-Delft Prediction dev-kit, based on the nuScenes dev-kit.
# Code written by Holger Caesar, 2018.
# Modified by Hidde Boekema, 2024.

import argparse
import os

from tqdm import tqdm

from vod import VOD


def verify_setup(vod_: VOD):
    """
    Script to verify that the VOD installation is complete.
    """

    # Check that each sample_data file exists.
    print('Checking that sample_data files are complete...')
    for sd in tqdm(vod_.sample_data):
        file_path = os.path.join(vod_.dataroot, sd['filename'])
        assert os.path.exists(file_path), 'Error: Missing sample_data at: %s' % file_path

    # Check that each map file exists.
    print('Checking that map files are complete...')
    for map_ in tqdm(vod_.map):
        file_path = os.path.join(vod_.dataroot, map_['filename'])
        assert os.path.exists(file_path), 'Error: Missing map at: %s' % file_path


if __name__ == "__main__":

    # Settings.
    parser = argparse.ArgumentParser(description='Test that the installed dataset is complete.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dataroot', type=str, default='/data/sets/vod',
                        help='Default VOD data directory.')
    parser.add_argument('--version', type=str, default='v1.0-trainval',
                        help='Which version of the VoD dataset to evaluate on, e.g. v1.0-trainval.')
    parser.add_argument('--verbose', type=int, default=1,
                        help='Whether to print to stdout.')

    args = parser.parse_args()
    dataroot = args.dataroot
    version = args.version
    verbose = bool(args.verbose)

    # Init.
    vod_ = VOD(version=version, verbose=verbose, dataroot=dataroot)

    # Verify data blobs.
    verify_setup(vod_)
