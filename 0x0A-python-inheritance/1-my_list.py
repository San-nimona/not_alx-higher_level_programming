#!/usr/bin/python3
"""Defines an inherited list class."""


class MyList(list):
    """Implements sorted printing 4 the built-in lst class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
