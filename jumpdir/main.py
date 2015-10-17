from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from jumpdir.directories import Directories
from jumpdir.pathfinder import PathFinder
from jumpdir.bookmarks import Bookmarks

import argparse
import os
import sys

HOME = os.getenv('HOME')
BOOKMARKS = os.path.join(HOME, '.jdbookmarks.json')

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
                        help='directory to search for (case insensitive).',
                        )
    parser.add_argument('-b', '--bookmark',
                        help='bookmark a path to a directory under a given string',
                        )

    return parser.parse_args(args)


def create_bookmark(name, path):
    """
    Appends a bookmark to jumpdir's yaml file

    Args:
        name: name to save bookmark under
        path: path that bookmark points to
    Returns:
        None
    """
    if path == '.':
        print("CURRENT DIR")
        path = os.getcwd()
    elif path == '..':
        print("PARENT DIR")
        path = os.path.dirname(os.getcwd())

    bm = Bookmarks(BOOKMARKS)
    bm.add_bookmark(name, path)
    bm.save_bookmarks()
    print("Bookmarked path '{0}' under '{1}'".format(path, name))
    sys.exit()


def main():
    """
    Retrieve user's search term from sys.args, create a list of all directories within
    user's home path, then compare each directory name against the search_term.

    Returns:
        The path to the first matching directory, or None if no match is found.
    """
    args = parse_args(sys.argv[1:])

    if args.bookmark is not None:
        create_bookmark(args.search_term, args.bookmark)

    search_term = args.search_term

    pfinder = PathFinder(search_term)
    dlist = Directories(HOME)
    for d in dlist:
        if pfinder.check_path(d):
            return d

if __name__ == '__main__':
    main()
