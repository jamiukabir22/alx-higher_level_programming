#!/usr/bin/python3
"""
A function that returns True if the object is ecactly
an instance f specified class else False.
"""


def inherits_from(obj, a_class):
    """Return True or False"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
