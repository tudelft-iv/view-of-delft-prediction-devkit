# View-of-Delft Prediction dev-kit, based on the nuScenes dev-kit.
# Code written by Oscar Beijbom, 2019.
# Modified by Hidde Boekema, 2024.

import os
import unittest

from vod import VOD


class TestVOD(unittest.TestCase):

    def test_load(self):
        """
        Loads up VOD.
        This is intended to simply run the VOD class to check for import errors, typos, etc.
        """

        assert 'VOD' in os.environ, 'Set VOD env. variable to enable tests.'
        vod_ = VOD(version='v1.0-mini', dataroot=os.environ['VOD'], verbose=False)

        # Trivial assert statement
        self.assertEqual(vod_.table_root, os.path.join(os.environ['VOD'], 'v1.0-mini'))


if __name__ == '__main__':
    unittest.main()
