# Small Python line counter script

## Objective

* Create a small Python script with real world use case
* Naïve implementation, nothing too sophisticated
* Present lines of code per language (based on file extension)
* Take directory name as input and recurse through that directory

## Useful tools

* `uv`, see [README.md](../README.md) one directory up from here
  * `uv` can be used as replacement for previous Python package managers
    * provides useful `uv tool install` and `uv tool run` commands to install and run Python utilities, e.g.
      * `cookiecutter` a tool allowing to template projects and use those templates to bootstrap, e.g. Python projects
      * `ruff` a Python formatter _and_ linter and so much more
        * can also be installed with `winget install -e --id astral-sh.ruff` from an elevated prompt
      * `black` a Python formatter from the Python Software Foundation (PSF) sticking to PEP8

## What we've done

### First session (2025-09-24)

* Learned a few details about importing
* What's a package and module and what's the role of `__init__.py` and other files inside a package
* Recap of f-strings and how to use `f"{varname=}"` or `f"{varname=!r}"`
* Arguments come in via `sys.argv` list
  * First element is the script name itself
  * `sys.argv[1:]` contains the remainder
  * passing `*sys.argv[1:]` to a function "expands" the list and passes the items one by one
  * the `*args` in a function declaration like `def func(*args):` captures the passed (positional) arguments in a list named `args`
* Practical use of the `Path` class from the `pathlib` standard library module
  * using `pathlib.Path.open()` in a `with` compound statement
* Initializing a set using a literal: `extensions = {".cs", ".pas", ".c", ".h"}`
* Condition to check membership in a set
* Walrus operator (`:=`) to adhoc declare _and_ assign a variable in loop constructs
