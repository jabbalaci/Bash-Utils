#!/usr/bin/env python

import os
import sys
import shutil

CWD = os.getcwd()
TEMPLATES = os.path.abspath(os.path.dirname(sys.argv[0])) + '/' + 'templates'


def copy(ext, full_name=None):
    if full_name:
        source = full_name
    else:
        source = 'alap.' + ext
    #
    if os.path.isfile(CWD + '/' + source):
        print >>sys.stderr, 'Warning: {} already exists in the current directory.'.format(source)
        sys.exit(1)
    # else
    shutil.copyfile(TEMPLATES + '/' + source, CWD + '/' + source)
    if os.path.isfile(CWD + '/' + source):
        print '# {} is created'.format(source)
        return 0    # OK
    else:
        print "Warning: couldn't copy {}.".format(source)
        return 1    # problem


def main():
    print """---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) C      [c]
3) D      [d]
4) Java   [java]
q) quit"""
    while True:
        try:
            ch = raw_input('> ')
        except (EOFError, KeyboardInterrupt):
            print
            ch = 'q'
        if ch in ['1', 'py']:
            sys.exit(copy('py'))
        elif ch in ['2', 'c']:
            sys.exit(copy('c'))
        elif ch in ['3', 'd']:
            sys.exit(copy('d'))
        elif ch in ['4', 'java']:
            sys.exit(copy('java', full_name='Alap.java'))
        elif ch == 'q':
            print 'bye.'
            sys.exit(0)
        else:
            print 'Wat?'

#############################################################################

if __name__ == "__main__":
    main()
