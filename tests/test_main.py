import os
import unittest
import shutil

import jumpdir

from tools import capture_sys_output, create_dtree
from example_dtrees import example_home_dir

class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_path = os.getcwd()
        os.mkdir('Mock_Home')
        cls.mock_home_path = os.path.join(cls.base_path, 'Mock_Home')
        create_dtree(example_home_dir, cls.mock_home_path)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.mock_home_path)

    def test_parse_args_parses_search_term(self):
        args = jumpdir.main.parse_args(['django'])
        search_term = args.search_term

        self.assertEqual('django', search_term)

    def test_parse_args_with_empty_args(self):
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output() as (stdout, stderr):
                jumpdir.main.parse_args([])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 2)

    def test_parse_args_with_multiple_args(self):
        with self.assertRaises(SystemExit) as cm:
            with capture_sys_output() as (stdout, stderr):
                jumpdir.main.parse_args(['one', 'two'])

        exit_exception = cm.exception
        self.assertEqual(exit_exception.code, 2)

    def test_search_for_directory_name_containing_spaces(self):
        pfinder = jumpdir.pathfinder.PathFinder('DAVID BOWIE')
        dlist = jumpdir.dir_list.DirectoryList(self.mock_home_path)

        self.assertIn(True, [pfinder.check_path(d) for d in dlist])

if __name__ == '__main__':
    unittest.main()
