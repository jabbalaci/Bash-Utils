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

Samples:

    /boot $ top10
    17458360 ./initrd.img-3.11.0-18-generic
    17456508 ./initrd.img-3.11.0-17-generic
    17451581 ./initrd.img-3.11.0-15-generic
    17303009 ./initrd.img-3.11.0-13-generic
    17302636 ./initrd.img-3.11.0-14-generic
    16397540 ./initrd.img-3.8.0-32-generic
    5634192 ./vmlinuz-3.11.0-18-generic
    5631792 ./vmlinuz-3.11.0-17-generic
    5631120 ./vmlinuz-3.11.0-15-generic
    5601072 ./vmlinuz-3.11.0-14-generic

    /boot $ top10 -h
    16.65M ./initrd.img-3.11.0-18-generic
    16.65M ./initrd.img-3.11.0-17-generic
    16.64M ./initrd.img-3.11.0-15-generic
    16.50M ./initrd.img-3.11.0-13-generic
    16.50M ./initrd.img-3.11.0-14-generic
    15.64M ./initrd.img-3.8.0-32-generic
    5.37M ./vmlinuz-3.11.0-18-generic
    5.37M ./vmlinuz-3.11.0-17-generic
    5.37M ./vmlinuz-3.11.0-15-generic
    5.34M ./vmlinuz-3.11.0-14-generic

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
