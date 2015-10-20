import json
import os


class Bookmarks:
    "Used to load, save and manipulate bookmark data from a json file"
    def __init__(self, fname):
        self.jfile = fname
        self.load_bookmarks()

    def __iter__(self):
        return iter(self.bm_dict)

    def __getitem__(self, key):
        return self.bm_dict[key]

    def add_bookmark(self, name, path):
        "Add a name:path bookmark to bookmark dictionary"
        self.bm_dict[name] = path
        self.save_bookmarks()
        print("Bookmarked path '{0}' under '{1}'".format(path, name))

    def del_bookmark(self, name):
        "Checks saved bookmarks for matching bookmark and deletes it if it exists"
        if name in self.bm_dict.keys():
            del self.bm_dict[name]
            print("Deleted bookmark '{0}'".format(name))
        else:
            print("Could not find bookmark '{0}'".format(name))
        self.save_bookmarks()

    def load_bookmarks(self, jfile=None):
        "Load json data from a file into object's bm_dict"
        if jfile is None:
            jfile = self.jfile

        if os.path.exists(jfile):
            with open(jfile, 'r') as jfile:
                self.bm_dict = json.loads(jfile.read())
        else:
            with open(jfile, 'w') as jfile:
                self.bm_dict = {}

    def save_bookmarks(self, jfile=None):
        "Save dictionary of bookmarks to jfile"
        if jfile is None:
            jfile = self.jfile
        with open(jfile, "w") as jfile:
            jdata = json.dumps(self.bm_dict, sort_keys=True,
                               indent=4, separators=(',', ': '))
            jfile.write(jdata)

    def list_bookmarks(self):
        "List all bookmarks in bm_dict"
        if len(self.bm_dict) == 0:
            print("No bookmarks saved")
        else:
            print("Jumpdir Bookmarks:")
            for name in self.bm_dict:
                print("\t\033[92m{0}\033[0m : {1}".format(name,
                                                          self.bm_dict[name]))
