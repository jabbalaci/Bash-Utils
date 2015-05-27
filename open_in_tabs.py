#!/usr/bin/env python2

"""
Open URLs in tabs
=================
Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/03/09/open-urls-in-browser-tabs-simultaneously/
GitHub:  https://github.com/jabbalaci/Bash-Utils

Read URLs from the standard input and open them in separated tabs.

Usage:
------
cat url_list.txt | ./open_in_tabs.py

Options:
  -n, --new-window      Open URLs in a new browser window.
  -s, --simultaneously  Open URLs simultaneously.

Warning! The combination -ns is experimental!
"""

import webbrowser
import sys
import commands
import shlex

from optparse import OptionParser
from subprocess import call
from time import sleep

__version__ = '0.3.0'

FIREFOX = webbrowser.get('firefox')
FIREFOX_PROCESS = 'firefox'         # look for it in the output of 'ps'
FIREFOX_EXE = 'firefox'                 # Firefox executable
DELAY = 3.0                             # seconds


def is_firefox_running():
    output = commands.getoutput('ps ux')
    return FIREFOX_PROCESS in output


def open_in_new_window(url, options, arguments):
    if options.simultaneously:
        command = "{0} -new-window {1}".format(FIREFOX_EXE, url)
        call(shlex.split(command))
        sleep(DELAY)
    else:
        FIREFOX.open_new(url)


def open_in_new_tab(url, options, arguments):
    if options.simultaneously:
        command = "{0} -new-tab {1}".format(FIREFOX_EXE, url)
        call(shlex.split(command))
    else:
        FIREFOX.open_new_tab(url)


def main():
    parser = OptionParser(usage='%prog [options]', version=__version__)

    #[options]
    parser.add_option('-n',
                      '--new-window',
                      action='store_true',
                      default=False,
                      help='Open URLs in a new browser window.')
    parser.add_option('-s',
                      '--simultaneously',
                      action='store_true',
                      default=False,
                      help='Open URLs simultaneously.')

    options, arguments = parser.parse_args()

    if options.new_window and options.simultaneously:
        print >>sys.stderr, \
            "# {0}: this combination is experimental.".format(sys.argv[0])
        #sys.exit(2)

    if not is_firefox_running():
        print >>sys.stderr, \
            "{0}: error: firefox is not running.".format(sys.argv[0])
        sys.exit(1)

    first = True
    for url in sys.stdin.readlines():
        url = url.rstrip("\n")

        if options.new_window:
            if first:
                open_in_new_window(url, options, arguments)
                first = False
            else:
                open_in_new_tab(url, options, arguments)
        else:
            open_in_new_tab(url, options, arguments)

    return 0

if __name__ == '__main__':
    sys.exit(main())
