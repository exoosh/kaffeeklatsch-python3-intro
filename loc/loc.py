#!/usr/bin/env python3
import sys
from pathlib import Path
from collections import defaultdict

# import humptydumpty
# ^--- uncomment to see modules at work, this only works with modern Python 3.x
# first executes top-level expressions in humptydumpty/__init__.py
# name that is available is 'humptydumpty' and symbols under it as humptydumpty.*
#
# alternatively one could use:
# from humptydumpty import mod
# ^--- uncomment to see how we import mod from the humptydumpty package
# name that is available is 'mod' and symbols under it as mod.*
# Experiment: switch out mod for mod2 to import another part of the package


def count_non_empty(fileobj):
    linectr = 0
    while line := fileobj.readline():  # read line-wise
        # strip blank space (incl. \n) from both sides of string
        stripped_line = line.strip()
        # is the string non-empty?
        if stripped_line:
            linectr += 1  # actual counting of non-empty lines here (TODO)
    return linectr


def count(p):
    # NB: we open as binary so files that aren't UTF-8 encoded can be handled
    with p.open("rb") as f:  # open with context manager using pathlib.Path.open()
        linectr = count_non_empty(f)
        return linectr, p.suffix
    return None, None


def main(*args):
    extensions = {
        ".foo": "foobar baz",  # doesn't exist as "file type"
        ".cs": "C#",
        ".pas": "Pascal/Delphi",
        ".c": "C source",
        ".h": "C header",
    }  # this is a dict (type) literal
    # defaultdict creates a key upon access, default based on the type
    count_dict = defaultdict(int)
    for file_or_dir_path in args:  # iterate over command line arguments
        p = Path(file_or_dir_path)  # instantiate pathlib.Path from argument (str)
        # recursively glob through the path (globs are approx. wildcards)
        for p in p.rglob("*"):
            # for files with matching extension we proceed
            if p.is_file() and p.suffix in extensions:
                lines, suffix = count(p)  # ... to call the count() function
                if lines and suffix:
                    count_dict[suffix] += lines
    # iterating over a dictionary is done using the .items() method
    for extension, description in extensions.items():
        # If this is one of the extensions we care about, proceed
        if extension in count_dict:
            # output the "language description" and cumulative line count
            print(f"{description}: {count_dict[extension]}")


if __name__ == "__main__":
    # __name__ is a builtin variable containing the module name (here __main__ because this is the top-level script being executed)
    # print(f"Hello world from {__name__=} ({__file__=})")
    main(*sys.argv[1:])
