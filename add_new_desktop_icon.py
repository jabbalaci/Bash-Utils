#!/usr/bin/env python3

"""
A simple script that helps you create a desktop icon under Ubuntu.

Usage:
------

* put it into the folder ~/Desktop , enter ~/Desktop and launch it
* answer the questions and it'll create a launcher
* a launcher icon will appear on the Desktop

Author: Laszlo Szathmary (jabba.laci@gmail.com), 2022
"""

import os
import readline

TEMPLATE = """
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon[en_US]={icon}
Exec={exe}
Name[en_US]={name}
Comment[en_US]={name}
Name={name}
Comment={name}
Icon={icon}
""".strip()


def main():
    print(TEMPLATE)
    print()
    icon = "..."
    inp = input("Icon's path (press ENTER to skip): ").strip()
    if inp:
        icon = inp
    #
    exe = input("Exe's path: ").strip()
    if ' ' in exe:
        exe = f'"{exe}"'
    name = input("Short name that'll appear under the desktop icon: ").strip()
    print()

    result = TEMPLATE.format(icon=icon, exe=exe, name=name)

    fname = f"{name}.desktop"
    if os.path.isfile(fname):
        print(f"# {fname} already exists")
        print()
        print(result)
    else:
        with open(fname, "w") as to:
            to.write(result)
        os.system(f'chmod u+x "{fname}"')
        #
        print(f"# {fname} was created")
    #

##############################################################################

if __name__ == "__main__":
    main()
