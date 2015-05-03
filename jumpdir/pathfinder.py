from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

class PathFinder:
    """
    Used to analyse paths for a match with given string.
    """

    def __init__(self, search_term):
        self.search_term = search_term

    def check_path(self, path):
        dir_name = self.get_dir_name(path)
        if dir_name.lower() == self.search_term.lower():
            return True
        else:
            return False

    def get_dir_name(self, path):
        idx = 0
        for char in path[::-1]:
            idx -= 1
            if char == '/':
                return path[idx + 1:]
 
