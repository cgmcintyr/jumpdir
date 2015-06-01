import os
import unittest
import shutil

from jumpdir.dir_list import DirectoryList

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

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_path)

    def test_DirectoryList_initialises_with_root_attribute_of_type_str(self):
        dlist = DirectoryList(self.test_path)

        self.assertEqual(type(dlist.root), str)

    def test_DirectoryList_initialises_with_correct_root_attribute(self):
        dlist = DirectoryList(self.test_path)

        self.assertEqual(dlist.root, self.test_path)

    def test_DirectoryList_initialises_with_dirs_attribute_of_type_list(self):
        dlist = DirectoryList(self.test_path)

        self.assertEqual(type(dlist.dirs), list)

    def test_DirectoryList_is_iterable(self):
        dlist = DirectoryList(self.test_path)

        self.assertCountEqual(iter(dlist), dlist.dirs)

    def test_list_builder_method_returns_list_of_correct_length(self):
        dirs = DirectoryList(self.test_path).list_builder(self.test_path)

        self.assertEqual(len(dirs), 6)

    def test_list_builder_recursively_creates_a_list_of_directory_names(self):
        dirs = DirectoryList(self.test_path).list_builder(self.test_path)

        self.assertIn(os.path.join(self.test_path, 'first', 'example'), dirs)
        self.assertIn(os.path.join(self.test_path, 'second'), dirs)

    def test_list_builder_ignores_directories_beginning_with_a_period(self):
        dirs = DirectoryList(self.test_path).list_builder(self.test_path)

        self.assertNotIn(os.path.join(self.test_path, '.hidden'), dirs)

if __name__ == '__main__':
    unittest.main()
