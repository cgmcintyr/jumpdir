from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from jumpdir.directories import Directories
from jumpdir.pathfinder import PathFinder
from jumpdir.bookmarks import Bookmarks

import argparse
import os
import sys

HOME = os.getenv('HOME')
DATA_DIR = os.path.join(HOME, '.jumpdir')
BOOKMARKS = os.path.join(DATA_DIR, '.jdbookmarks.json')
CACHE_FILE = os.path.join(DATA_DIR, '.jdcache.json')

if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

def parse_args(args):
    """Parse list/tuple of arguments with argparse module

    - **Parameters** and **returns**::
        :param list args: arguments to be parsed
        :returns namespace: parsed arguments
    """
    parser = argparse.ArgumentParser(description='jumpdir')
    subparsers = parser.add_subparsers(help='sub-command help',
                                       dest='commands')

    # jumpdir search ...
    parser_search = subparsers.add_parser('search',
            help='search home directory for a directory matching given search term')
    parser_search.add_argument('search_term',
            help='directory name to search for (case insensitive).',)
    parser_search.set_defaults(which='search')

    # jumpdir add ...
    parser_add = subparsers.add_parser('add', help='add bookmark')
    parser_add.add_argument('name', help='name of bookmark to add')
    parser_add.add_argument('-p', '--path', default=os.getcwd(),
            help="define path that bookmark points to")

    # jumpdir delete ...
    parser_delete = subparsers.add_parser('delete', help='delete bookmark')
    parser_delete.add_argument('name', help='name of bookmark to remove')

    # jumpdir list ...
    subparsers.add_parser('list', help='list saved bookmarks')

    return parser.parse_args(args)


def run_search(search_term, bookmarks):
    if search_term == HOME:
        return HOME

    pfinder = PathFinder(search_term)

    # Search through bookmarks
    for dname in bookmarks:
        if pfinder.check_match(dname):
            return bookmarks[dname]

    # Search cached dirs
    ddict = Directories(HOME, CACHE_FILE)
    for dname in ddict:
        if pfinder.check_match(dname):
            return ddict.shallowest_path_to(dname)

    # Search home folder and update cache
    ddict.map_directories()
    for dname in ddict:
        if pfinder.check_match(dname):
            return ddict.shallowest_path_to(dname)


def main(argv=sys.argv[1:]):
    if len(argv) < 1:
        raise ValueError("error: no commands given")
    args = parse_args(argv)
    bookmarks = Bookmarks(BOOKMARKS)

    # Sub command logic
    if not args.commands:
        raise ValueError("error: command not recognised")
    elif args.commands == 'add':
        bookmarks.add_bookmark(args.name, args.path)
        raise SystemExit
    elif args.commands == 'delete':
        bookmarks.del_bookmark(args.name)
        raise SystemExit
    elif args.commands == 'list':
        bookmarks.list_bookmarks()
        raise SystemExit
    else:
        return run_search(args.search_term, bookmarks)


if __name__ == '__main__':
    main()
