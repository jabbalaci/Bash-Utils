#!/usr/bin/env python3

"""
Misc. utils.
"""

import random


def my_shuffle(array):
    """
    Returns a shuffled array.

    random.shuffle shuffles in place and returns None. This way shuffle can be
    used in a chain.
    """
    random.shuffle(array)
    return array


def inc_string(text):
    """
    Increase a string by one.

    Examples: a -> b, e -> f, z -> aa, af -> ag.
    """
    text = list(text[::-1])
    go_over = False
    for index, c in enumerate(text):
        if index == 0 or go_over:
            up = chr(ord(c)+1)
        if up <= 'z':
            go_over = False
            text[index] = up
            break
        else:
            go_over = True
            text[index] = 'a'

    if go_over:
        text.append('a')

    return ''.join(text[::-1])


def pretty_num(n):
    """
    Converts a number to a nicely formatted string.

    Example: 6874 => '6,874'.
    """
    return "{:,}".format(n)


def filesize_fmt(num):
    """
    Human-readable file size.
    http://stackoverflow.com/questions/1094841
    """
    for x in ['b', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    return "%3.1f %s" % (num, 'TB')

##############################################################################

if __name__ == "__main__":
    print(my_shuffle(['a', 'b', 'c'])[0])
    #
    print('a ->', inc_string('a'))
    print('f ->', inc_string('f'))
    print('z ->', inc_string('z'))
    print('af ->', inc_string('af'))
    print('zz ->', inc_string('zz'))
    #
    number = 6874
    print(pretty_num(number))   # '6,874'
    #
    length = 1322688512
    print(filesize_fmt(length))
