#!/usr/bin/env python3

"""
An interactive script to
1) compress a directory and store the archive in another folder, and
2) uncompress an archive to a given folder

Supported archiving / compression methods:
* tar
* tgz
* zip

Contributors:
* Gábor Szőcs <https://github.com/szocs08>, zip support
"""

import os
import readline
import sys
from pathlib import Path

COMPRESS, UNCOMPRESS = (1, 2)
TAR, TGZ, ZIP = (3, 4, 5)
MODE = None    # will be set later


def die(msg):
    """
    Print an error message and terminate.
    """
    print(msg, file=sys.stderr)
    sys.exit(1)


def my_input(msg):
    """
    Take input from the user and handle Ctrl + c.
    """
    try:
        return input(msg)
    except (KeyboardInterrupt, EOFError):
        print()
        die("# abort")


def set_mode():
    """
    Handle symbolic links.

    If you put a symbolic link on this file called "be", then compression mode is selected.
    If you put a symbolic link on this file called "ki", then uncompression mode is selected.

    (be / ki means in / out in Hungarian, i.e. compress / uncompress)
    """
    global MODE
    p = Path(sys.argv[0])
    if p.name == 'be':
        MODE = COMPRESS
    if p.name == 'ki':
        MODE = UNCOMPRESS
    if MODE is None:
        inp = my_input("> compress or uncompress (c / u)? ")
        if inp == 'c':
            MODE = COMPRESS
        elif inp == 'u':
            MODE = UNCOMPRESS
        else:
            die("# error: unknown option")


def compress():
    """
    Compress a folder interactively.
    """
    print("# goal: compress a folder")
    while True:
        dname = my_input("> which folder to compress (ls: directory list)? ")
        if dname == 'ls':
            os.system("ls -ald */")    # show directories only
            print()
        else:
            break
    dname = Path(dname)
    if not dname.is_dir():
        die("error: it's not a directory")
    to_dir = Path(my_input("> where (in which directory) to store the archive file? "))
    if not to_dir.is_dir():
        to_dir.mkdir()
        if not to_dir.is_dir():
            die("# error: couldn't create the directory")
        print("# directory created")
    #
    accepted = ["tar", "tgz", "zip"]
    while True:
        ext = my_input("> what compression to use ({})? ".format(", ".join(accepted)))
        if ext not in accepted:
            print("# unknown format")
        else:
            break
    #
    tar_options = "cvf"
    if ext == "tgz":
        tar_options = "cvzf"
    if ext in ["tar", "tgz"]:
        fname = str(dname) + ".tgz"
        cmd = "tar {options} {to_dir}/{fname} {dname}".format(options=tar_options,
                                                              to_dir=str(to_dir),
                                                              fname=fname,
                                                              dname=dname)
        print("# " + cmd)
        os.system(cmd)
    zip_options = "-r"
    if ext == "zip":
        fname = str(dname) + ".zip"
        cmd = "zip {options} {to_dir}/{fname} {dname}".format(options=zip_options,
                                                              to_dir=str(to_dir),
                                                              fname=fname,
                                                              dname=dname)
        print("# " + cmd)
        os.system(cmd)


def uncompress():
    """
    Uncompress an archive file interactively.
    """
    print("# goal: uncompress an archive file")
    while True:
        fname = my_input("> which file to uncompress (ls: directory list)? ")
        if fname == 'ls':
            os.system('ls -al | grep -v "^d"')    # show files only
            print()
        else:
            break
    fname = Path(fname)
    if not fname.is_file():
        die("error: it's not a file")
    #
    ftype = None    # file type: tar, tgz, zip
    s = str(fname)
    if s.endswith(".tar"):
        ftype = TAR
    elif s.endswith((".tar.gz", ".tgz")):
        ftype = TGZ
    elif s.endswith(".zip"):
        ftype = ZIP
    else:
        die("# error: unknown file extension")
    #
    to_dir = Path(my_input("> where to uncompress the archive file (give a directory name)? "))
    if not to_dir.is_dir():
        to_dir.mkdir()
        if not to_dir.is_dir():
            die("# error: couldn't create the directory")
        print("# directory created")
    #
    tar_options = "xvf"
    if ftype == TGZ:
        tar_options = "xvzf"
    if ftype in [TAR, TGZ]:
        cmd = "tar {options} {fname} -C {to_dir}".format(options=tar_options,
                                                         to_dir=str(to_dir),
                                                         fname=fname)
        print("# " + cmd)
        os.system(cmd)
    if ftype == ZIP:
        cmd = "unzip {fname} -d {to_dir}".format(options=tar_options,
                                                         to_dir=str(to_dir),
                                                         fname=fname)
        print("# " + cmd)
        os.system(cmd)


def main():
    set_mode()
    if MODE == COMPRESS:
        compress()
    else:
        uncompress()

##############################################################################

if __name__ == "__main__":
    main()
