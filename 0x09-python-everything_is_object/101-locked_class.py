#!/usr/bin/python3
"""
Defines a class with no class or object attribute
Control dynamically created instance attributes
https://www.python-course.eu/python3_slots.php
"""


class LockedClass():
    """
    prevents user from creating new instance attribute dynamically
    unless attribute is "first_name"
    >>> a = LockedClass()
    >>> a.first_name = 'Aisha'
    >>> a.first_name
    'Aisha'
    >>> a.last_name = 'Ammah'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name
    """

    __slots__ = "first_name"
