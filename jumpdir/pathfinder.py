from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os


class PathFinder:
    "Used to check for matches against a given string"

    def __init__(self, string):
        self.string = string

    def check_match(self, dname):
        ""
        if dname.lower() == self.string.lower():
            return True
        else:
            return False
