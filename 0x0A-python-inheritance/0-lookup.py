#!/usr/bin/python3
"""Defs an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attr"""
    return (dir(obj))
