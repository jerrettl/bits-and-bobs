#!/usr/bin/python3


"""
> tfw you realize this is already in python but you make it from
scratch anyway
> that's not getting fixed unless it absolutely should
"""


def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def isindex(name, index):
    try:
        name[index]
        return True
    except IndexError:
        return False
