from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from jumpdir.dir_list import DirectoryList
from jumpdir.pathfinder import PathFinder

import argparse
import os
import sys

HOME = os.getenv('HOME')

def parse_args(args):
    """
    Parse list/tuple of arguments with argparse module. 

    Args:
        args (list/tuple): arguments to be parsed.
    
    Returns:
        Namespace of parsed args.
    """
    parser = argparse.ArgumentParser(description='jumpdir')
    parser.add_argument('search_term',
                        help='Directory to search for (case insensitive).'
                        )
    return parser.parse_args(args)

def main():
    """
    Retrieve user's search term from sys.args, create a list of all directories within
    user's home path, then compare each directory name against the search_term.
    
    Returns:
        The path to the first matching directory, or None if no match is found.
    """
    args = parse_args(sys.argv[1:])
    search_term = args.search_term

    pfinder = PathFinder(search_term)
    dlist = DirectoryList(HOME)
    for d in dlist:
        if pfinder.check_path(d):
            return d

if __name__ == '__main__':
    main()

