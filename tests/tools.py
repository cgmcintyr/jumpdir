from contextlib import contextmanager
import os
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

@contextmanager
def capture_sys_output():
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr  = current_out, current_err

def create_dtree(dir_dict, path):
    """
    Creates a directory tree in given path by recursivly walking through a nested
    dictionary of directory names.
    """
    called_from = os.getcwd()

    for branch in list(dir_dict):
        os.chdir(path)
        try:
            os.mkdir(branch)
            os.chdir(branch)
            create_dtree(dir_dict[branch], os.path.join(path, branch))
        except TypeError:
            # No directory to create
            continue

    os.chdir(called_from)
