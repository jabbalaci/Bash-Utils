#!/usr/bin/env python

import os
import sys
import shutil

CWD = os.getcwd()
TEMPLATES = os.path.abspath(os.path.dirname(sys.argv[0])) + '/' + 'templates'
EXECUTABLE = ['py', 'd']


def rename(fname):
    dirName, fileName = os.path.split(fname)
    fileExt = os.path.splitext(fileName)[1]
    #
    reply = raw_input("New name of the file (without extension) [ENTER to cancel]: ")
    if reply:
        to_name = dirName + '/' + reply + fileExt
        os.rename(fname, to_name)
        if os.path.isfile(to_name):
            print '# renamed to', os.path.split(to_name)[1]


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
    dest = CWD + '/' + source
    shutil.copyfile(TEMPLATES + '/' + source, dest)
    if os.path.isfile(dest):
        print '# {} is created'.format(source)
        if ext in EXECUTABLE:
            os.chmod(dest, 0700)
    else:
        print "Warning: couldn't copy {}.".format(source)
        sys.exit(1)    # problem
        
    rename(dest)


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
            copy('py')
            break
        elif ch in ['2', 'c']:
            copy('c')
            break
        elif ch in ['3', 'd']:
            copy('d')
            break
        elif ch in ['4', 'java']:
            copy('java', full_name='Alap.java')
            break
        elif ch == 'q':
            print 'bye.'
            sys.exit(0)
        else:
            print 'Wat?'

#############################################################################

if __name__ == "__main__":
    main()
