#!/usr/bin/env python

"""
Markdown previewer
==================
Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/05/05/readme-markdown-on-github/
GitHub:  https://github.com/jabbalaci/Bash-Utils

Preview markdown files.

Usage:
------
Put it in your ~/bin directory (make sure ~/bin is in your PATH), 
make it executable (chmod u+x ~/bin/markdown.py), and call it as 
“markdown.py README.markdown“. It will open the HTML output in a 
new browser tab. Adding the “-u” switch (update), the HTML is not 
opened in the browser.
"""

import os
import sys

MARKDOWN = 'markdown'
UPSKIRT = 'upskirt'

PROGRAM = UPSKIRT

def main():
    update = False

    if len(sys.argv) < 2:
        print "Usage: {0} <file.markdown> [-u]".format(sys.argv[0])
        sys.exit(1)
    # else
    if '-u' in sys.argv:
        update = True
        sys.argv.remove('-u')
    input_file = sys.argv[1]
    os.system("{program} {input} > /tmp/markdown.html".format(program=PROGRAM, input=input_file))
    if not update:
        os.system("chromium-browser /tmp/markdown.html &")

main()
