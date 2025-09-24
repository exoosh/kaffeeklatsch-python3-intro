#!/usr/bin/env python3
import sys
from pathlib import Path

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


def count(p):
    extensions = {".cs", ".pas", ".c", ".h"}  # this is a set (type) literal
    if p.suffix in extensions:  # this tests membership in the set
        with p.open() as f:  # open with context manager using pathlib.Path.open()
            while line := f.readline():  # read line-wise
                # print(f"{line=!r}") # debug output
                # strip blank space (incl. \n) from both sides of string
                stripped_line = line.strip()
                # print(f"{stripped_line=!r}") # debug output
                # is the string non-empty?
                if stripped_line:
                    ...  # actual counting of non-empty lines here (TODO)


def main(*args):
    for file_or_dir_path in args:  # iterate over command line arguments
        p = Path(file_or_dir_path)  # instantiate pathlib.Path from argument (str)
        # recursively glob through the path (globs are approx. wildcards)
        for path_item in p.rglob("*"):
            if path_item.is_file():  # for files we proceed
                count(path_item)  # ... to call the count() function
                break  # just here temporarily  break after the first file
        break  # just here temporarily  to break after the first command line arg


if __name__ == "__main__":
    # __name__ is a builtin variable containing the module name (here __main__ because this is the top-level script being executed)
    # print(f"Hello world from {__name__=} ({__file__=})")
    main(*sys.argv[1:])
