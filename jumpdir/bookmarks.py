import json
import os


class Bookmarks:
    """Used to load, save and manipulate bookmark data from a json file

    - **parameters** and  **instance variables**::

        :param str jfile: path to json file containing bookmark data
        :ivar str  jfile: copy of jfile paramater value
        :ivar dict bm_dict: *{str name: str path}* dictionary of bookmarks in jfile

    -  Notes
        * The keys of the bm_dict of a Bookmarks instance can be iterated over.
        * The value of an item in the bm_dict can be retrieved using ``self[key]``.
        * If using any of the above to manipulate the dictionary, changes are not
          saved to the bookmark jfile until ``self.save_bookmarks()`` is called.
    """

    def __init__(self, jfile):
        self.jfile = jfile
        self.bm_dict = {}
        self.load_bookmarks()

    def __iter__(self):
        return iter(self.bm_dict)

    def __getitem__(self, key):
        return self.bm_dict[key]

    def add_bookmark(self, name, path):
        """Add a bookmark to given path under name, replacing any previous bookmark

        - **parameters** and **returns**::

            :param str name: name to save the bookmark under in jfile
            :param str path: absolute path to a directory
            :returns None:

        """
        self.bm_dict[name] = path
        self.save_bookmarks()
        print("Bookmarked path '{0}' under '{1}'".format(path, name))

    def del_bookmark(self, name):
        """Checks saved bookmarks for matching bookmark and deletes it if it exists

        - **parameters** and **returns**::

            :param str name: name of bookmark to delete from jfile
            :returns None:

        """
        if name in self.bm_dict.keys():
            del self.bm_dict[name]
            print("Deleted bookmark '{0}'".format(name))
        else:
            print("Could not find bookmark '{0}'".format(name))
        self.save_bookmarks()

    def load_bookmarks(self, jfile=None):
        """Load json data from a file into object's bm_dict

        - **parameters** and **returns**::

            :param str jfile: path to bookmark json file to load, defaults to instance's jfile
            :returns None:

        """
        if jfile is None:
            jfile = self.jfile

        if os.path.exists(jfile):
            with open(jfile, 'r') as jfile:
                self.bm_dict = json.load(jfile)
        else:
            with open(jfile, 'w') as jfile:
                self.bm_dict = {}
                json.dump(self.bm_dict,  jfile)

    def save_bookmarks(self, jfile=None):
        """Save dictionary of bookmarks to jfile

        - **parameters** and **returns**::

            :param str jfile: path to bookmark json file to save to, defaults to instance's jfile
            :returns None:

        """
        if jfile is None:
            jfile = self.jfile
        with open(jfile, "w") as jfile:
            json.dump(self.bm_dict, jfile, sort_keys=True,
                      indent=4, separators=(',', ': '))

    def list_bookmarks(self):
        """List all bookmarks in bm_dict

        - **parameters** and **returns**::

            :returns None:

        """
        if len(self.bm_dict) == 0:
            print("No bookmarks saved")
        else:
            print("Jumpdir Bookmarks:")
            for name in self.bm_dict:
                print("\t\033[92m{0}\033[0m : {1}".format(name,
                                                          self.bm_dict[name]))
