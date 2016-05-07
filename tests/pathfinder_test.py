import unittest

from jumpdir.pathfinder import PathFinder

from tests.tools import capture_sys_output

class MainTest(unittest.TestCase):

    def test_intialise_PathFinder_with_string(self):
        pfinder = PathFinder('test')
        self.assertEqual(pfinder.string, 'test')

    def test_exception_when_intialising_PathFinder_without_arguments(self):
        self.assertRaises(TypeError, PathFinder)

    def test_exception_when_intialising_PathFinder_multiple_arguments(self):
        self.assertRaises(TypeError, PathFinder, 'arg', 'arg2')

    def test_check_match_method_returns_true_if_dir_name_matches_string(self):
        string = dirname = 'test'
        pfinder = PathFinder(string)
        pfinder_result = pfinder.check_match(dirname)

        self.assertEqual(pfinder_result, True)

    def test_check_match_method_returns_false_if_dir_name_does_not_match_string(self):
        string = 'fails'
        dirname = "test"
        pfinder = PathFinder(string)
        pfinder_result = pfinder.check_match(dirname)

        self.assertEqual(pfinder_result, False)

    def test_check_match_method_is_case_insensitive(self):
        string = 'TeSt'
        dirname = "test"
        pfinder = PathFinder(string)
        pfinder_result = pfinder.check_match(dirname)

        self.assertEqual(pfinder_result, True)


if __name__ == '__main__':
    unittest.main()
