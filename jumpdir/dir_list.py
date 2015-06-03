from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

class DirectoryList:
    """
    Recursivley create and stores list of paths to directories under given base directory. 
    
    Attributes:
        base (str)  = top directory to work down from.
        dirs (list) = flat list of paths to all non-hidden directores under base directory.
    """

    def __init__(self, base):
        self.base = base
        self.dirs = self.list_builder(base)

    def __iter__(self):
        return iter(self.dirs)

    def list_builder(self, base_dir):
        """
        Recursively creates the list of paths to all directories under given directory.

        Args:
            base_dir: path of directory to look for subdirectories in.
        
        Returns:
            flat list of paths to all non-hidden directories under base_dir. 
        """
        dirs = []

        for f in os.listdir(dir_path):
            try:
                # Python2
                f = unicode(f)
            except NameError:
                # Python3
                pass

            if f.startswith('.'):
                continue

            fpath = os.path.join(root, f)
            if os.path.isdir(fpath):
                dirs.append(fpath)

                for d in self.list_builder(fpath):
                    dirs.append(d)

        return dirs

