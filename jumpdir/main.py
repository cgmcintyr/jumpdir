from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

try:
    input = raw_input
except NameError:
    pass

from jumpdir.dir_list import DirectoryList
from jumpdir.pathfinder import PathFinder

import argparse
import os
import sys

HOME = os.getenv('HOME')

parser = argparse.ArgumentParser(description='jumpdir')
parser.add_argument('search_term', help='Directory name to search for.')

def main():
    """
    Main entry point for jumpdir. Currently returns the first matching
    directory.
    """
    args = parser.parse_args()

    dlist = DirectoryList(HOME)
    search_term = args.search_term
    pfinder = PathFinder(search_term)
    for d in dlist:
        if pfinder.check_path(d):
            print(d)
            break

if __name__ == '__main__':
    main()

