from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import json
import os
from collections import defaultdict


class Directories:
    """Used to build dictionary of directory names and corresponding paths

    Recursivley creates and stores a dict of directory names and a list of
    corresponding paths below a given root directory.

    - **parameters** and  **instance variables**::

        :param str base_dir : path to root directory
        :param str cache_file: path to json directory cache file
        :ivar defaultdict dirs: *{str directory name: list paths}* dictionary
            of directory names and corresponding paths
    """

    def __init__(self, base_dir, cache_file):
        self.base_dir = base_dir # Top level directory to start from
        self.cache_file = cache_file
        self.dirs = {}
        self.load_cache(cache_file)

    def __getitem__(self, key):
        return self.dirs[key]

    def __iter__(self):
        return iter(self.dirs)

    def map_directories(self):
        self.dirs = defaultdict(list)
        self.dict_builder(self.base_dir)
        self.cache_dirs(self.cache_file)

    def dict_builder(self, base_dir):
        """Walks through base_dir and populates instance's  dirs defaultdict

        - **parameters** and **returns**::
            :param str base_dir: path to root directory
            :returns None
        """
        try:
            for f in os.listdir(base_dir):
                try:
                    # Python2
                    f = unicode(f)
                except NameError:
                    # Python3
                    pass

                if f.startswith('.'):
                    continue

                fpath = os.path.join(base_dir, f)
                if os.path.isdir(fpath):
                    self.dirs[f.lower()].append(fpath)
                    self.dict_builder(fpath)
        except OSError:
            # Permission denied
            return

    def shallowest_path_to(self, dname):
        """Returns the shallowest path from corresponding paths in dirs dictionary

        - **parameters** and **returns**::
            :param str dname: directory name to retrieve path from
            :returns str: shallowest path from corresponding list of paths
        """
        return sorted(self.dirs[dname], key=len)[0]

    def cache_dirs(self, cache_file):
        """Saves current directory dictionary as json file
        - **parameters** and **returns**::
            :param str cache_file: location of file to save to
            :returns None
        """
        if cache_file is None:
            cache_file = self.cache_file
        with open(cache_file, "w") as cache_file:
            json.dump(self.dirs, cache_file, sort_keys=True,
                      indent=4, separators=(',', ': '))

    def load_cache(self, cache_file):
        """Loads a directory dictionary from a json file
        - **parameters** and **returns**::
            :param str cache_file: location of file to load
            :returns None
        """
        if cache_file is None:
            cache_file = self.cache_file
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as cache_file:
                self.dirs = json.load(cache_file)
        else:
            with open(cache_file, 'w') as cache_file:
                self.dirs = {}
                json.dump(self.dirs, cache_file)
