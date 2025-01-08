import sys

# See https://peps.python.org/pep-0655/#usage-in-python-3-11
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict
else:
    # for Python <3.11 with (Not)Required
    from typing_extensions import NotRequired, TypedDict  # noqa: F401
