import json


class Bookmarks:
    """
    Used to load, save and manipulate bookmark json data

    Attributes:
        bmdict (dict): dictionary of bookmarks in name:path form
        jfile (str): path to json file containing bookmark data
    """
    def __init__(self, fname):
        self.bmdict = self.load_bookmarks(fname)
        self.jfile = fname

    def add_bookmark(self, name, path):
        """
        Add a name:path bookmark to object's bookmark dictionary

        Args:
            name (str): name of bookmark
            path (str): path to directory that will be bookmarked
        """
        self.bmdict[name] = path

    def del_bookmark(self, name):
        """
        Checks a object's bmdict  for a {name:path} bookmark. If it exists the
        bookmark is deleted, otherwise the dictionary is returned as is.

        Args:
            name (str): name of bookmark
        """
        if name in self.bmdict.keys():
            del self.bmdict[name]

    def load_bookmarks(self, jfile=None):
        """
        Load json data from a file into object's bmdict

        Args:
            jfile (str): path to file containing json data
        """
        if jfile is None:
            jfile = self.jfile
        with open(jfile, 'r') as jfile:
            self.bmdict = json.loads(jfile.read())

    def save_bookmarks(self, jfile=None):
        """
        Save dictionary of bookmarks to jfile

        Args:
            jfile (str): path to jfile to save to
        """
        if jfile is None:
            jfile = self.jfile
        with open(jfile, "w") as jfile:
            jdata = json.dumps(self.bmdict, sort_keys=True,
                               indent=4, separators=(',', ': '))
            jfile.write(jdata)
