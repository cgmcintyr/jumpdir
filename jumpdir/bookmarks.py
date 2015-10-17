import json
import os

class Bookmarks:
    """
    Used to load, save and manipulate bookmark json data

    Attributes:
        bm_dict (dict): dictionary of bookmarks in name:path form
        jfile (str): path to json file containing bookmark data
    """
    def __init__(self, fname):
        self.jfile = fname
        self.load_bookmarks()

    def add_bookmark(self, name, path):
        """
        Add a name:path bookmark to object's bookmark dictionary

        Args:
            name (str): name of bookmark
            path (str): path to directory that will be bookmarked
        """
        self.bm_dict[name] = path

    def del_bookmark(self, name):
        """
        Checks a object's bm_dict  for a {name:path} bookmark. If it exists
        the bookmark is deleted from object's bm_dict.

        Args:
            name (str): name of bookmark
        """
        if name in self.bm_dict.keys():
            del self.bm_dict[name]

    def load_bookmarks(self, jfile=None):
        """
        Load json data from a file into object's bm_dict

        Args:
            jfile (str): path to file containing json data
        """
        if jfile is None:
            jfile = self.jfile

        if os.path.exists(jfile):
            with open(jfile, 'r') as jfile:
                self.bm_dict = json.loads(jfile.read())
        else:
            with open(jfile, 'w') as jfile:
                self.bm_dict = {}

    def save_bookmarks(self, jfile=None):
        """
        Save dictionary of bookmarks to jfile

        Args:
            jfile (str): path to jfile to save to
        """
        if jfile is None:
            jfile = self.jfile
        with open(jfile, "w") as jfile:
            jdata = json.dumps(self.bm_dict, sort_keys=True,
                               indent=4, separators=(',', ': '))
            jfile.write(jdata)
