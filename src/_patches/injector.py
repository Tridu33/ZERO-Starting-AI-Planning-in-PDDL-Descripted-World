# Patch for Brevitas 0.12.x incompatibility with the newest _dependencies package.
#
# This file is the canonical source. Apply by replacing the installed copy at:
#     <your-venv>/lib/python3.X/site-packages/_dependencies/checks/injector.py
#
# Usage (one-liner):
#
#     cp _patches/injector.py \
#        "$(python -c 'import sys; print(sys.prefix)')/lib/python$(python -c 'import sys; print(sys.version_info[0]).\".\"+str(sys.version_info[1]))')/site-packages/_dependencies/checks/injector.py"
#
# Or simply edit the installed file manually and replace _check_dunder_name.

# -*- coding: utf-8 -*-
from _dependencies.exceptions import DependencyError


def _check_inheritance(bases, injector):

    for base in bases:
        if not issubclass(base, injector):
            message = "Multiple inheritance is allowed for Injector subclasses only"
            raise DependencyError(message)


def _check_dunder_name(name):
    # Patch: brevitas 0.12.1 defines injector classes with dunder names; allow them.
    return


def _check_attrs_redefinition(name):

    if name == "let":
        raise DependencyError("'let' redefinition is not allowed")
