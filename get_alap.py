#!/usr/bin/env python

import os
import sys
import shutil

CWD = os.getcwd()
TEMPLATES = os.path.abspath(os.path.dirname(sys.argv[0])) + '/' + 'templates'
EXECUTABLE = ['py', 'd']
EDITOR = 'vim'


def rename(fname):
    dirName, fileName = os.path.split(fname)
    fileExt = os.path.splitext(fileName)[1]
    #
    reply = raw_input("New name of the file (without extension) [ENTER to cancel]: ").strip()
    if reply:
        to_name = dirName + '/' + reply + fileExt
        os.rename(fname, to_name)
        if os.path.isfile(to_name):
            print '# renamed to', os.path.split(to_name)[1]
            return to_name
        else:
            return None
    else:
        return fname


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

    return rename(dest)


def edit(fname):
    ch = raw_input("Do you want to edit the file [y/n] (default: y)? ").strip()
    if ch=='y' or ch=='':
        os.system('{ed} "{f}"'.format(ed=EDITOR, f=fname))


def main():
    print """---------------------------
Create an empty source file
---------------------------
1) Python [py]
2) Go     [go]
3) Java   [java]
4) C      [c]
5) D      [d]
q) quit"""
    while True:
        try:
            ch = raw_input('> ')
        except (EOFError, KeyboardInterrupt):
            print
            ch = 'q'
        if ch in ['1', 'py']:
            return copy('py')
            break
        elif ch in ['2', 'go']:
            return copy('go')
            break
        elif ch in ['3', 'java']:
            return copy('java', full_name='Alap.java')
            break
        elif ch in ['4', 'c']:
            return copy('c')
            break
        elif ch in ['5', 'd']:
            return copy('d')
            break
        elif ch == 'q':
            print 'bye.'
            sys.exit(0)
        else:
            print 'Wat?'

#############################################################################

if __name__ == "__main__":
    fname = main()
    edit(fname)
