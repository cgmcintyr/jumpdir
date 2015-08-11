from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

class DirectoryList:
    """
    Recursivley create and stores list of paths to directories under given base directory. 
    
    Attributes:
        base_dir (str)  = absolute path to top directory to work down from.
        dirs (list)     = flat list of absolute paths to all non-hidden directores
                          under the base directory.
    """

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.dirs = self.list_builder(base_dir)

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
                dirs.append(fpath)

                for d in self.list_builder(fpath):
                    dirs.append(d)

        return dirs

