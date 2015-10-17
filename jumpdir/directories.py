from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

from collections import defaultdict


class Directories:
    """
    Recursivley create and stores list of paths to directories under given base directory.

    Attributes:
        base_dir (str)  = absolute path to top directory to work down from.
        dirs (list)     = flat list of absolute paths to all non-hidden directores
                          under the base directory.
    """

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.dirs = defaultdict(list)
        self.dict_builder(base_dir)

    def __iter__(self):
        return iter(self.dirs)

    def dict_builder(self, base_dir):
        """
        Recursively walks through base_dir and creates dictionary of all
        non-hidden directory names and their corresponding paths

        Args:
            base_dir (str): path of directory to look for subdirectories in.
        """
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
                self.dirs[f].append(fpath)
                self.dict_builder(fpath)

