#!/usr/bin/env python

"""
Image to BASE64
===============

Take an image file and encode it with BASE64. Put the encoded data in
an "img" HTML tag.

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/04/17/embed-images-in-html-pages/
GitHub:  https://github.com/jabbalaci/Bash-Utils

Usage:
------

./img_to_base64.py <image_file>
    By default, the data is nested in an HTML tag and the output
    is wrapped. These settings can be customized.
    The output is printed to the standard output.

Sample output:
--------------

<img class='inline-image' src='data:image/gif;base64,R0lGODlhIgAbAPMPAGxsbNbW1v
/rhf/ge//3kf/Ub9/f3/b29oeHh/7LZv/0juazTktLS8WSLf//mf///yH5BAAAAAAALAAAAAAiABsAA
ASA8MlJq7046827/2AojiTVnI1xlFZjBisruU7tPCiqjg2h/L9KA2HgCQS5pE7UGLgwAhyCWWjYrrWE
owFgJqyEsDi82HZDja/jyGaXuV7rYE6fv8+gtLXA7/OtcCEGSoQMUyEHAQgAjI2OAAgBIwcGAZaXmAE
7Mpydnp+goaKjFBEAOw==' />
"""

import sys
import imghdr
import base64
import textwrap

# you can change the 'class' attribute or you can add more attributes
TEMPLATE = "<img class='inline-image'" + \
           " src='data:image/{0};base64,{1}' />"

# format options
HTML = 1        # one line, nested in TEMPLATE
BASE64 = 2      # one line, pure base64 encoded output
HTML_WRAP = 3   # wrapped HTML output, nested in TEMPLATE

# width fot text wrap
HTML_WRAP_WIDTH = 79


def convert_to_base64(filename, image_type, format=HTML):
    """Read the image file and encode it with base64.

    Return the image file either in an HTML img tag or as plain base64 text.
    """
    img = open(filename, 'rb')
    data = base64.b64encode(img.read())
    img.close()

    if format in [HTML, HTML_WRAP]:
        text = TEMPLATE.format(image_type, data)
        if format == HTML_WRAP:
            text = '\n'.join(textwrap.wrap(text, HTML_WRAP_WIDTH))
        return text
    # else
    if format == BASE64:
        return data
    # else
    return ''


def main(args):
    """Verify the format of the input file and print the base64 encoded text.

    Supported file formats: 'png' and 'jpeg'.
    """
    filename = args[0]
    image_type = imghdr.what(filename)

    if image_type not in ['png', 'jpeg', 'gif']:
        print "{0}: image file should be PNG, JPG or GIF.".format(sys.argv[0])
        sys.exit(1)
    # else
    print convert_to_base64(filename, image_type, format=HTML_WRAP)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "{0}: missing image file argument.".format(sys.argv[0])
        sys.exit(0)
    else:
        main(sys.argv[1:])
