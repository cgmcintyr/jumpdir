from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os
from collections import defaultdict


class Directories:
    "Recursivley creates and stores a dict of directory names and a list of corresponding paths"

    def __init__(self, base_dir):
        self.base_dir = base_dir # Top level directory to start from
        self.dirs = defaultdict(list)
        self.dict_builder(base_dir)

    def __getitem__(self, key):
        return self.dirs[key]

    def __iter__(self):
        return iter(self.dirs)

    def dict_builder(self, base_dir):
        "Walks through base_dir and populates dirs defaultdict"
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

    def shallowest_path_to(self, dname):
        "Returns the shallowest path from corresponding paths in dirs dictionary"
        return sorted(self.dirs[dname], key=len)[0]
