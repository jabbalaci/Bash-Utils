#!/usr/bin/env python2
# encoding: utf-8

"""
Get the public Dropbox links of several files
=============================================

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/06/01/get-the-public-dropbox-links-of-several-files/
GitHub:  https://github.com/jabbalaci/Bash-Utils (see the dropbox/ folder)

The script shows the public Dropbox link(s) of one (or several) file(s).

Usage:
======

get_public_link <file>      # show the link of <file>

or

get_public_link -a          # show the links of all files in the current directory

If you want to copy the links to the clipboard, combine it with tocb.py:

get_public_link <file> | tocb
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import hashlib
import os
import platform as p
import sys
import uuid
from optparse import OptionParser

#############################################################################

def string_to_md5(content):
    """Calculate the md5 hash of a string.

    This 'string' can be the binary content of a file too."""
    return hashlib.md5(content).hexdigest()


def get_fingerprint(md5=False):
    """
    Fingerprint of the current operating system/platform.

    If md5 is True, a digital fingerprint is returned.
    """
    sb = []
    sb.append(p.node())
    sb.append(p.architecture()[0])
    sb.append(p.architecture()[1])
    sb.append(p.machine())
    sb.append(p.processor())
    sb.append(p.system())
    sb.append(str(uuid.getnode()))    # MAC address
    text = '#'.join(sb)
    if md5:
        return string_to_md5(text)
    else:
        return text


def get_short_fingerprint(length=6):
    """
    A short digital fingerprint of the current operating system/platform.

    Length should be at least 6 characters.
    """
    assert 6 <= length <= 32
    #
    return get_fingerprint(md5=True)[-length:]

#############################################################################

# Your own Dropbox URL. No slash at the end.
BASE_URL = 'http://dl.dropbox.com/u/144888'
# Your own Dropbox/Public folder in the local file system. No slash at the end.
if get_short_fingerprint() in ('a804db'):
    BASE_PATH = '/trash2/Dropbox/Public'
else:
    BASE_PATH = '{home}/Dropbox/Public'.format(home=os.path.expanduser("~"))


def verify_file(abspath):
    """Verify if the entry exists and if it's a file (not a directory)."""
    if not os.path.isfile(abspath):
        print("Error: I/O problem with {0}.".format(abspath), file=sys.stderr)
        sys.exit(2)
    #
    verify_dir(os.path.split(abspath)[0])


def verify_dir(directory):
    """Verify if we are in the Dropbox/Public folder."""
    if "/Dropbox/Public" not in directory:
        print("Error: you are not in the Dropbox/Public folder....", file=sys.stderr)
        sys.exit(3)


def get_dropbox_link(abspath):
    """Get the public dropbox link of the file."""
    return abspath.replace(BASE_PATH, BASE_URL)


def process_file(file_name):
    """Process a single file."""
    f = os.path.abspath(file_name)
    verify_file(f)
    print(get_dropbox_link(f))


def process_curr_dir():
    """Process all the files in the current directory."""
    cwd = os.getcwd()
    verify_dir(cwd)
    for file_name in sorted(os.listdir(cwd)):
        if os.path.isfile(file_name):
            f = os.path.abspath(file_name)
            print(get_dropbox_link(f))


def check_constants():
    """Remove end slash if necessary."""
    global BASE_URL, BASE_PATH
    if BASE_URL.endswith('/'):
        BASE_URL = BASE_URL[:-1]
    if BASE_PATH.endswith('/'):
        BASE_PATH = BASE_PATH[:-1]


def main():
    """Controller."""

    check_constants()

    parser = OptionParser(usage='%prog <file> | -a')

    parser.add_option('-a',
                      '--all',
                      action='store_true',
                      default=False,
                      help='Get public links to all files in the current directory.')

    options, arguments = parser.parse_args()

    if len(arguments) == 0 and not options.all:
        parser.print_usage(),
        sys.exit(1)
    if len(arguments) > 0 and options.all:
        parser.print_usage(),
        sys.exit(1)

    # now either we have an argument xor we have the -a switch
    if len(arguments) > 0:
        process_file(arguments[0])

    if options.all:
        process_curr_dir()

#############################################################################

if __name__ == '__main__':
    main()
    # print(get_short_fingerprint())
