import os
import unittest
import shutil

import jumpdir

from tools import capture_sys_output, create_dtree
from example_dtrees import example_home_dir

class MainTest(unittest.TestCase):

    def setUp(self):
        self.base_path = os.getcwd()
        os.mkdir('Mock_Home')
        self.mock_home_path = os.path.join(self.base_path, 'Mock_Home')
        create_dtree(example_home_dir, self.mock_home_path)

    def tearDown(self):
        shutil.rmtree(self.mock_home_path)

    def test_takes_string_from_sysarg_and_returns_matching_directory(self):
        args = jumpdir.main.parse_sysargs(['django'])
        search_term = args.search_term
        self.assertEqual('django', search_term)

        pfinder = jumpdir.pathfinder.PathFinder(search_term)
        dlist = jumpdir.dir_list.DirectoryList(self.mock_home_path)

        self.assertIn(True, [pfinder.check_path(d) for d in dlist])

    def test_with_empty_args(self):
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output() as (stdout, stderr):
                jumpdir.main.parse_sysargs([])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 2)

    def test_with_multiple_args(self):
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output() as (stdout, stderr):
                jumpdir.main.parse_sysargs(['one', 'two'])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 2)

if __name__ == '__main__':
    unittest.main()
