#!/usr/bin/env python3

"""
picklecat: Concatenate or merge pickled Python 3 lists or dictionaries.

Usage:
    picklecat <pickle_file> <pickle_file>...

Options:
    -h --help   Show the documention.
    --version   Show version.
"""

from docopt import docopt

import sys
import pickle


__title__ = "picklecat"
__version__ = "1.0.0"
__description__ = "Concatenate or merge pickled Python 3 lists or dictionaries"
__license__ = "MIT"


def detect_type(content):
    """
    >>> detect_type([1, 2]) == list
    True

    >>> detect_type({"a": 1}) == dict
    True

    >>> detect_type(1) == "object"
    True
    """
    if isinstance(content, list):
        return list
    elif isinstance(content, dict):
        return dict
    else:
        return "object"


def _create_unit(pickle_type):
    if pickle_type == "object":
        return []
    else:
        return pickle_type()


def _concat_inplace(a, b, pickle_type):
    if pickle_type == "object":
        a.append(b)
    elif pickle_type == list:
        a.extend(b)
    elif pickle_type == dict:
        a.update(b)


def picklecat(*pickle_filenames):
    result = None
    pickle_type = None
    for filename in pickle_filenames:
        with open(filename, "rb") as f:
            content = pickle.load(f)
        if pickle_type is None:
            pickle_type = detect_type(content)
            result = _create_unit(pickle_type)
        _concat_inplace(result, content, pickle_type=pickle_type)
    return result


def main():
    args = docopt(__doc__, version=f"picklecat v{__version__}")
    vals = picklecat(*args["<pickle_file>"])
    sys.stdout.buffer.write(pickle.dumps(vals))


if __name__ == "__main__":
    main()
