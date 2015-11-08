from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os


class PathFinder:
    """Used to check for matches against an initialised string

    - **parameters** and **instance variables**::
        :param str string: string to compare matches against
        :ivar str string: copy of value in string param
    """

    def __init__(self, string):
        self.string = string

    def check_match(self, dname):
        """Check name of directory against string ivar

        - **parameters** and **instance variables**::
            :param str dname: name of directory
        """
        if dname.lower() == self.string.lower():
            return True
        else:
            return False
