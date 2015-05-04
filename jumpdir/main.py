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

def parse_sysargs(args):
    parser = argparse.ArgumentParser(description='jumpdir')
    parser.add_argument('search_term',
                        help='Directory to search for (case insensitive).'
                        )
    return parser.parse_args(args)

def main():
    """
    Create a list of all directories within user's home path, then search
    this list for a directory that matches the provided search_term.
    Return the first matching directory.
    """
    args = parse_sysargs(sys.argv[1:])
    search_term = args.search_term

    pfinder = PathFinder(search_term)
    dlist = DirectoryList(HOME)
    for d in dlist:
        if pfinder.check_path(d):
            return(d)

if __name__ == '__main__':
    main()

