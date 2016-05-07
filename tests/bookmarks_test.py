import json
import os
import unittest

from jumpdir.bookmarks import Bookmarks


class MainTest(unittest.TestCase):

    def setUp(self):
        self.test_json = '{"1": "t", "2": "tt", "3": "ttt"}'

        self.test_jfile = "test.json"
        with open(self.test_jfile, "w") as jfile:
            jfile.write(self.test_json)

        self.bm = Bookmarks(self.test_jfile)

    def tearDown(self):
        os.remove(self.test_jfile)

    def test_initialise_Bookmarks_with_jfile(self):
        self.assertEqual(self.bm.jfile, self.test_jfile)

    def test_load_bookmarks_loads_json_data_from_file(self):
        test_json = '{"this": "is", "a": "test"}'
        test_json_dict = json.loads(test_json)

        with open(self.test_jfile, "w") as jfile:
            jfile.write(test_json)
        self.bm.load_bookmarks()

        self.assertEqual(self.bm.bm_dict, test_json_dict)

    def test_load_bookmarks_works_with_missing_file(self):
        self.bm = Bookmarks("thisisnotafile.txt")

        self.assertEqual(self.bm.bm_dict, {})
        os.remove("thisisnotafile.txt")

    def test_jfile_data_is_loaded_into_bm_dict(self):
        with open(self.test_jfile, "r") as jfile:
            jdata = json.loads(jfile.read())

        self.assertEqual(self.bm.bm_dict, jdata)

    def test_del_bookmark_removes_bookmark_from_bm_dict(self):
        self.bm.del_bookmark(1)
        self.assertNotIn(1, self.bm.bm_dict.keys())

    def test_add_bookmark_inserts_bookmark_into_bm_dict(self):
        self.bm.add_bookmark("tttt", "/test/path")
        self.assertIn(("tttt", "/test/path"), self.bm.bm_dict.items())

    def test_save_bookmarks_writes_bm_dict_as_json_to_file(self):
        self.bm.bm_dict = {"first": "a", "second": "b", "third": "c"}
        self.bm.save_bookmarks()

        with open(self.test_jfile, "r") as jfile:
            jdata = json.loads(jfile.read())

        self.assertEqual(self.bm.bm_dict, jdata)

if __name__ == '__main__':
    unittest.main()
