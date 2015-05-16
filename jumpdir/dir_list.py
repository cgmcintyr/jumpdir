from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

class DirectoryList:
    """
    Recursively creates and stores a flat list of all non-hidden directory paths 
    under the provided root directory.
    """

    def __init__(self, root):
        self.root = root
        self.dirs = self.list_builder(root)

    def __iter__(self):
        return iter(self.dirs)

    def list_builder(self, root):
        dirs = []

        for f in os.listdir(root):
            try:
                f = unicode(f)
            except NameError:
                pass

            if f.startswith('.'):
                continue

            fpath = os.path.join(root, f)
            if os.path.isdir(fpath):
                dirs.append(fpath)

                for d in self.list_builder(fpath):
                    dirs.append(d)

        return dirs

