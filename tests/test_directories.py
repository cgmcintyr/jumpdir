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

    def create_mock_cache(path_to_cache_file):
        with open(path_to_cache_file, 'w') as f:
            f.write("{}")

    @classmethod
    def setUpClass(cls):
        cls.base_path = os.getcwd()
        os.mkdir('mock_dtree')
        cls.test_path = os.path.join(cls.base_path, 'mock_dtree')
        create_dtree(simple_dtree, cls.test_path)
        cls.mock_cache = os.path.join(cls.test_path, '.mockcache')
        cls.create_mock_cache(cls.mock_cache)
        cls.directories = Directories(cls.test_path, cls.mock_cache)
        cls.directories.map_directories()
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
        self.assertEqual(type(self.directories.base_dir), str)

    def test_Directories_initialises_with_correct_base_dir_attribute(self):
        self.assertEqual(self.directories.base_dir, self.test_path)

    def test_Directories_initialises_with_dirs_attribute_of_type_default_dict(self):
        self.assertEqual(type(self.directories.dirs), defaultdict)

    def test_Directories_is_iterable(self):
        self.assertCountEqual(iter(self.directories), self.directories.dirs.keys())

    def test_dict_builder_method_returns_dict_of_correct_length(self):
        self.assertEqual(len(self.directories.dirs), 6)

    def test_dict_builder_stores_directories_with_matching_names_under_same_key(self):
        self.assertEqual(len(self.directories.dirs['example']), 2)

    def test_dict_builder_stores_paths(self):
        self.assertIn(
            os.path.join(self.test_path, 'first', 'example'),
            self.directories.dirs['example'])

    def test_dict_builder_ignores_directories_beginning_with_a_period(self):
        self.assertNotIn('.hidden', self.directories.dirs.keys())

    def test_Directories_instances_are_subscriptable(self):
        self.assertEqual(self.directories['example'], self.directories.dirs['example'])

    def test_shallowest_path_to_returns_shortest_path_from_list(self):
        shallowest = self.directories.shallowest_path_to('example')
        is_shallowest = True
        for path in self.directories['example']:
            if (shallowest > path):
                is_shallowest = False
        self.assertTrue(is_shallowest)

if __name__ == '__main__':
    unittest.main()
