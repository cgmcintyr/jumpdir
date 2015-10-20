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
    subparsers = parser.add_subparsers(help='sub-command help', dest='commands')


    parser_search = subparsers.add_parser('search',
                                          help='search home directory for a directory matching given search term'
                                          )
    parser_search.add_argument('search_term', help='directory name to search for (case insensitive).',)
    parser_search.set_defaults(which='search')


    parser_add = subparsers.add_parser('add', help='add bookmark')
    parser_add.add_argument('name', help='name of bookmark to add')
    parser_add.add_argument('-p', '--path', default=os.getcwd(),
                            help="define path that bookmark points to"
                           )

    parser_delete = subparsers.add_parser('delete', help='delete bookmark')
    parser_delete.add_argument('name',
                               help='name of bookmark to remove'
                              )

    parser_list = subparsers.add_parser('list', help='list saved bookmarks')

    return parser.parse_args(args)


def create_bookmark(name):
    """
    Appends a bookmark to jumpdir's yaml file

    Args:
        name: name to save bookmark under
        path: path that bookmark points to
    Returns:
        None
    """
    bm = Bookmarks(BOOKMARKS)
    bm.add_bookmark(name, os.getcwd())
    bm.save_bookmarks()
    print("Bookmarked path '{0}' under '{1}'".format(os.getcwd(), name))
    sys.exit()


def delete_bookmark(name):
    bm = Bookmarks(BOOKMARKS)
    bm.del_bookmark(name)
    bm.save_bookmarks()
    print("Removed bookmark '{0}'".format(name))
    sys.exit()


def list_bookmarks():
    bm = Bookmarks(BOOKMARKS)
    print("Jumpdir Bookmarks:")
    for name in bm:
        print("\t\033[92m{0}\033[0m : {1}".format(name, bm[name]))
    sys.exit()


def main():
    """
    Retrieve user's search term from sys.args, create a list of all directories within
    user's home path, then compare each directory name against the search_term.

    Returns:
        The path to the first matching directory, or None if no match is found.
    """
    args = parse_args(sys.argv[1:])

    if args.commands == 'add':
        create_bookmark(args.name)
    elif args.commands == 'delete':
        delete_bookmark(args.name)
    elif args.commands == 'list':
        list_bookmarks()
    elif args.commands == 'search':
        pass

    if args.search_term == HOME:
        return HOME

    search_term = args.search_term
    pfinder = PathFinder(search_term)

    # Check if search_term is a bookmark
    bm = Bookmarks(BOOKMARKS)
    for dname in bm:
        if pfinder.check_match(dname):
            return bm[dname]

    ddict = Directories(HOME)
    for dname in ddict:
        if pfinder.check_match(dname):
            # Return the shallowest matching path
            return ddict.shallowest_path_to(dname)

if __name__ == '__main__':
    main()
