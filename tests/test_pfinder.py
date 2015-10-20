import unittest

from jumpdir.pathfinder import PathFinder

from tools import capture_sys_output

class MainTest(unittest.TestCase):

    def test_intialise_PathFinder_with_string(self):
        pfinder = PathFinder('test')
        self.assertEqual(pfinder.string, 'test')

    def test_exception_when_intialising_PathFinder_without_arguments(self):
        self.assertRaises(TypeError, PathFinder)

    def test_exception_when_intialising_PathFinder_with_multiple_arguments(self):
        self.assertRaises(TypeError, PathFinder, 'arg', 'arg2')

    def test_check_match_method_returns_true_if_dir_name_matches_string(self):
        string = 'test'
        test_dname = "test"
        pfinder = PathFinder(string)
        pfinder_result = pfinder.check_match(test_dname)

        self.assertEqual(pfinder_result, True)

    def test_check_match_method_returns_false_if_dir_name_does_not_match_string(self):
        string = 'fails'
        test_dname = "test"
        pfinder = PathFinder(string)
        pfinder_result = pfinder.check_match(test_dname)

        self.assertEqual(pfinder_result, False)

    def test_check_match_method_is_case_insensitive(self):
        string = 'TeSt'
        test_dname = "test"
        pfinder = PathFinder(string)
        pfinder_result = pfinder.check_match(test_dname)

        self.assertEqual(pfinder_result, True)


if __name__ == '__main__':
    unittest.main()
