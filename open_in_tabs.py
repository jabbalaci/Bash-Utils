#!/usr/bin/env python3

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

Last update: 2017-01-08 (yyyy-mm-dd)
"""

import shlex
import sys
import webbrowser
from optparse import OptionParser
from subprocess import call
from time import sleep

from lib.process import get_simple_cmd_output

__version__ = '0.3.0'

FIREFOX = webbrowser.get('firefox')
FIREFOX_PROCESS = 'firefox'         # look for it in the output of 'ps'
FIREFOX_EXE = 'firefox'                 # Firefox executable
DELAY = 3.0                             # seconds


def is_firefox_running():
    output = get_simple_cmd_output('ps ux')
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
        print("# {0}: this combination is experimental.".format(sys.argv[0]), file=sys.stderr)
        #sys.exit(2)

    if not is_firefox_running():
        print("{0}: error: firefox is not running.".format(sys.argv[0]), file=sys.stderr)
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

#############################################################################

if __name__ == '__main__':
    sys.exit(main())
