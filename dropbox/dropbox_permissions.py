#!/usr/bin/env python

"""
Setting file permissions in your Dropbox folder recursively
===========================================================

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/05/08/setting-file-permissions-in-your-dropbox-folder-recursively/
GitHub:  https://github.com/jabbalaci/Bash-Utils (see the dropbox folder)

This script will change permissions only if permissions are not
correct. 
If we traverse our Dropbox folder recursively and set
permissions everywhere, Dropbox will synchronize ALL the files!
This script solves this problem by not modifying directories/files
whose permissions are good.

The Windows version of the Dropbox software regularly removes the 
executable flags. This script corrects that problem too.

Intended audience:
------------------
Linux users who also use Windows sometimes.

Usage:
------
Customize the header part, put the script in the root of your Dropbox
folder and launch it. Set DRY to False if you want to apply the
changes.
"""

import os
import sys
import stat

# dry run, make no changes just show them
DRY = True
#DRY = False

# verify if we are in the Dropbox folder
VERIFY_DROPBOX = True
#VERIFY_DROPBOX = False

# don't do anything with these folders:
ignore_dirs = ('.git', '.svn', '.eric4project', '.ropeproject')
# files with this extension will be executable:
executable_file_extensions = ('.py', '.sh', '.pl')
# these files will be executable:
executable_files_with_relative_path = (
    './xmind-portable/XMind_Linux/xmind',
    './xmind-portable/XMind_Linux/xmind-bin',
    './git.projects/others/upskirt/upskirt'
)

# some counters:
symlinks = 0
changes = 0


def chmod_ux(file):
    """Make a file executable.
    
    Apply chmod u+x on the file."""
    set_mode_to(file, 0700)


def set_mode_to(file, permissions):
    """Set the file with the given permissions."""
    global changes
    f = file
    mode = get_oct_mode(f)
    if mode != oct(permissions):
        try:
            if DRY:
                print "# chmod {0} {1}".format(oct(permissions), f)
            else:
                os.chmod(f, permissions)
            changes += 1
        except OSError:
            print >>sys.stderr, "# cannot chmod the file {0}".format(f)


def get_oct_mode(entry):
    """Get the permissions of an entry in octal mode.
    
    The return value is a string (ex. '0600')."""
    entry_stat = os.stat(entry)
    mode = oct(entry_stat[stat.ST_MODE] & 0777)
    return mode


def process_dir(directory):
    """Set the permissions of a directory."""
    set_mode_to(directory, 0700)


def process_file(file):
    """Set the permissions of a file."""
    f = file
    file_name = os.path.split(f)[1]
    file_ext = os.path.splitext(file_name)[1]

    if (file_ext in executable_file_extensions) or (f in executable_files_with_relative_path):
        process_exe_file(f)
    else:
        process_other_file(f)


def process_exe_file(file):
    """The file will be executable."""
    chmod_ux(file)


def process_other_file(file):
    """Normal file, not executable."""
    set_mode_to(file, 0600)


def skip_symlink(entry):
    """Symlinks are skipped.
    
    Imagine that you have a symlink that points out of your Dropbox folder to
    your HOME for instance. If we followed symlinks, the script would process
    your HOME directory too. We want the script to stay strictly in your
    Dropbox folder."""
    global symlinks
    symlinks += 1
    print "# skip symlink {0}".format(entry)


def traverse(directory):
    """Traverse directory recursively. Symlinks are skipped."""
    #content = [os.path.abspath(os.path.join(directory, x)) for x in os.listdir(directory)]
    content = [os.path.join(directory, x) for x in os.listdir(directory)]
    dirs = sorted([x for x in content if os.path.isdir(x)])
    files = sorted([x for x in content if os.path.isfile(x)])

    for d in dirs:
        if os.path.islink(d):
            skip_symlink(d)
            continue
        dir_name = os.path.split(d)[1]
        if dir_name in ignore_dirs:
            continue
        # else
        process_dir(d)
        traverse(d)
    
    for f in files:
        if os.path.islink(f):
            skip_symlink(f)
            continue
        # else
        process_file(f)


def verify_dir(directory):
    """ Verify if we are in the Dropbox folder."""
    d = os.path.abspath(directory)
    if 'dropbox' not in d.lower():
        print >>sys.stderr, """
It seems that you are not in the Dropbox folder. If you launch this
script in a wrong folder, it may do more harm than good since it
changes file permissions recursively.
If this is a false alarm and you really want to execute the script
here, disable this verification by setting the variable VERIFY_DROPBOX
to False.
"""
        sys.exit(1)


def main():
    """Controller."""
    start_dir = '.'
    if VERIFY_DROPBOX:
        verify_dir(start_dir)
    process_dir(start_dir)
    traverse(start_dir)
    #chmod_ux(sys.argv[0])
    print "# skipped symlinks: {0}".format(symlinks)
    print "# changes: {0}".format(changes)
    if DRY:
        print "# >>> it was a dry run, no changes were made <<<"

#############################################################################

if __name__ == "__main__":
    main()
