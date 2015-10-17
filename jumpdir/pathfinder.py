from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os


class PathFinder:
    """
    Used to analyse paths for a match with initialised search term.

    Attributes:
        search_term (str): string to check directory names against.
    """

    def __init__(self, search_term):
        self.search_term = search_term

    def check_match(self, dname):
        """
        Retrieve the file/directory name and compare it with the search term.

        Args:
            dname: name of directory/file to be checked.

        Returns:
            True if there is a direct match (case insensitive), False otherwise.
        """
        if dname.lower() == self.search_term.lower():
            return True
        else:
            return False
