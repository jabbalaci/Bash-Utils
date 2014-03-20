#!/usr/bin/env python3
# encoding: utf-8

"""
Show the top 10 largest files in the current directory.
Bash command:

    find . -printf '%s %p\n'| sort -nr | head -10

Problem: it shows filesizes in bytes.

This script adds support to show filesizes
in a human-readable format.

Usage:

    # classical output in bytes
    ./top10.py

    # improved, human-readable output
    ./top10.py -h

Requires Python 3.
"""

import locale
import shlex
import subprocess as sp
import sys

encoding = locale.getdefaultlocale()[1]
HUMAN_READABLE = False


def sizeof_fmt(num):
    """
    Convert file size to human readable format.
    """
    for x in ['b', 'K', 'M', 'G', 'T']:
        if num < 1024.0:
            return "{0:.2f}{1}".format(num, x)
        num /= 1024.0


def human_readable(lines):
    for line in lines:
        num, fname = line.split(maxsplit=1)
        num = sizeof_fmt(int(num))
        print('{n} {f}'.format(n=num, f=fname))


def main():
    find = sp.Popen(shlex.split("find . -printf '%s %p\n'"), stdout=sp.PIPE)
    sort = sp.Popen(shlex.split("sort -nr"),
            stdin=find.stdout, stdout=sp.PIPE, stderr=sp.PIPE)
    out = sort.communicate()[0].decode(encoding).split("\n")
    out = out[:10]
    if HUMAN_READABLE:
        human_readable(out)
    else:
        for line in out:
            print(line)

##############################################################################

if __name__ == "__main__":
    if '-h' in sys.argv[1:]:
        HUMAN_READABLE = True
    #
    main()
