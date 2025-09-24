# This file inside a directory makes that directory a package
#
# The file can technically be empty. But all its top-level code will get executed upon 'import',
# such as the print() below.

# __name__ is a builtin variable containing the module name (here humptydumpty based on the containing directory)
print(f"Hello world from {__name__=} ({__file__=})")

# Experiment, run the following to see how the __name__ changes when this is called as top-level script:
# py -3 .\__init__.py
