import os
import unittest
import shutil

from jumpdir.directories import Directories

from tools import capture_sys_output, create_dtree

simple_dtree = {
    'first': {
        'example': None,
        },
    'second': {
        'toot toot': None,
        'bootboot': {
            'jam_recipes': None,
            },
        },
    '.hidden': None,
}

class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_path = os.getcwd()
        os.mkdir('mock_dtree')
        cls.test_path = os.path.join(cls.base_path, 'mock_dtree')
        create_dtree(simple_dtree, cls.test_path)

        try:
            # Python2
            cls.assertCountEqual = cls.assertItemsEqual
        except AttributeError:
            # Python3
            pass

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_path)

    def test_Directories_initialises_with_base_dir_attribute_of_type_str(self):
        dlist = Directories(self.test_path)

        self.assertEqual(type(dlist.base_dir), str)

    def test_Directories_initialises_with_correct_base_dir_attribute(self):
        dlist = Directories(self.test_path)

        self.assertEqual(dlist.base_dir, self.test_path)

    def test_Directories_initialises_with_dirs_attribute_of_type_list(self):
        dlist = Directories(self.test_path)

        self.assertEqual(type(dlist.dirs), list)

    def test_Directories_is_iterable(self):
        dlist = Directories(self.test_path)

        self.assertCountEqual(iter(dlist), dlist.dirs)

    def test_list_builder_method_returns_list_of_correct_length(self):
        dirs = Directories(self.test_path).list_builder(self.test_path)

        self.assertEqual(len(dirs), 6)

    def test_list_builder_recursively_creates_a_list_of_directory_names(self):
        dirs = Directories(self.test_path).list_builder(self.test_path)

        self.assertIn(os.path.join(self.test_path, 'first', 'example'), dirs)
        self.assertIn(os.path.join(self.test_path, 'second'), dirs)

    def test_list_builder_ignores_directories_beginning_with_a_period(self):
        dirs = Directories(self.test_path).list_builder(self.test_path)

        self.assertNotIn(os.path.join(self.test_path, '.hidden'), dirs)

if __name__ == '__main__':
    unittest.main()