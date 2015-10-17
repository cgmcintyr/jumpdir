import os
import unittest
import shutil

from collections import defaultdict

from jumpdir.directories import Directories

from tools import create_dtree

simple_dtree = {
    'first': {
        'example': None,
        },
    'second': {
        'toot toot': None,
        'bootboot': {
            'jam_recipes': None,
            },
        'example': None,
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
        ddict = Directories(self.test_path)

        self.assertEqual(type(ddict.base_dir), str)

    def test_Directories_initialises_with_correct_base_dir_attribute(self):
        ddict = Directories(self.test_path)

        self.assertEqual(ddict.base_dir, self.test_path)

    def test_Directories_initialises_with_dirs_attribute_of_type_list(self):
        ddict = Directories(self.test_path)
        self.assertEqual(type(ddict.dirs), defaultdict)

    def test_Directories_is_iterable(self):
        ddict = Directories(self.test_path)

        self.assertCountEqual(iter(ddict), ddict.dirs.keys())

    def test_dict_builder_method_returns_dict_of_correct_length(self):
        dirs = Directories(self.test_path).dirs

        self.assertEqual(len(dirs), 6)

    def test_dict_builder_stores_directories_with_matching_names_under_same_key(self):
        dirs = Directories(self.test_path).dirs

        self.assertEqual(len(dirs['example']), 2)

    def test_dict_builder_stores_paths(self):
        dirs = Directories(self.test_path).dirs

        self.assertIn(
            os.path.join(self.test_path, 'first', 'example'),
            dirs['example'])

    def test_dict_builder_ignores_directories_beginning_with_a_period(self):
        dirs = Directories(self.test_path).dirs

        self.assertNotIn('.hidden', dirs.keys())

if __name__ == '__main__':
    unittest.main()
