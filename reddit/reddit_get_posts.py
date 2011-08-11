#!/usr/bin/env python

"""
Reddit, get posts
=================

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://ubuntuincident.wordpress.com/2011/08/11/browse-your-favorite-subreddits-painlessly/
GitHub:  https://github.com/jabbalaci/Bash-Utils

This script can extract links to posts in a subreddit.
You can get links to comments (-c switch) or 
to direct URLs (-u switch).

Basic usage:
------------

./reddit_get_posts.py -c /r/earthporn
    Get links to comments of subreddit "earthporn".

./reddit_get_posts.py -u /r/earthporn
    Get links to direct URLs of subreddit "earthporn".

./reddit_get_posts.py -u http://www.reddit.com/r/earthporn
    You can specify the complete URL of the subreddit.

./reddit_get_posts.py -u http://www.reddit.com/r/EarthPorn/?count=25&after=t3_jffyd
    You can even browse pages on reddit.com.

./reddit_get_posts.py -u
    Extract links of your favourite subreddit (specify it with the constant DEFAULT_REDDIT).


Advanced usage:
---------------

This script can be used together with another script of mine called open_in_tabs.py, which
is part of this Bash-Utils project too. open_in_tabs.py can open the extracted links in
your Firefox instance. Example:

./reddit_get_posts.py -u /r/earthporn | open_in_tabs -s
    This will open the links simultaneously (-s switch) in Firefox.
"""

import urlparse
import urllib
import json
import sys

from optparse import OptionParser

# no trailing slash:
BASE = 'http://www.reddit.com'
# This one can be customized. No trailing slash:
DEFAULT_REDDIT = 'http://www.reddit.com/r/nsfw'

# don't hurt these constants:
REDDIT = DEFAULT_REDDIT
COMMENTS = 'permalink'
URL = 'url'
WHAT_TO_GET = ''


def init():
    global REDDIT
    REDDIT = REDDIT + '/.json'


def get_json_text():
    page = REDDIT
    print >>sys.stderr, "#", page
    sock = urllib.urlopen(page)
    json_text = sock.read()
    return json_text


def process_post(index, post):
    # indexing starts with 1 (instead of 0):
    index += 1
    print urlparse.urljoin(BASE, post['data'][WHAT_TO_GET])


def process_posts(decoded):
    posts = decoded['data']['children']
    for i,post in enumerate(posts):
        process_post(i, post)


def verify_options(options):
    if not options.comments and not options.url:
        print >>sys.stderr, "{0}: you must specify what to extract.".format(sys.argv[0])
        sys.exit(1)

    if options.comments and options.url:
        print >>sys.stderr, "{0}: decide which one to extract.".format(sys.argv[0])
        sys.exit(1)


def verify_arguments(arguments):
    if len(arguments) > 1:
        print >>sys.stderr, \
            "{0}: you must specify one reddit in one of the following forms:\n\
/r/reddit or\n\
http://www.reddit.com/r/reddit".format(sys.argv[0])
        sys.exit(1)

    global REDDIT

    if len(arguments) == 1:
        arg = arguments[0]
        if arg.startswith('/r/'):
            REDDIT = "{base}{reddit}/.json".format(base=BASE, reddit=arg)
        elif arg.startswith('http'):
            REDDIT = arg
            REDDIT = REDDIT.replace('/?', '/.json?')
            if '/.json' not in REDDIT:
                REDDIT = REDDIT + '/.json'
        else:
            print >>sys.stderr, "{0}: argument error. It should look like /r/reddit or http://www.reddit.com/r/reddit .".format(sys.argv[0])
            sys.exit(1)


def main():
    init()
    parser = OptionParser(usage='%prog [options] [reddit]')

    #[options]
    parser.add_option('-c',
                      '--comments',
                      action='store_true',
                      default=False,
                      help='Get comment links.')
    parser.add_option('-u',
                      '--url',
                      action='store_true',
                      default=False,
                      help='Get URL links.')

    options, arguments = parser.parse_args()

    verify_options(options)
    verify_arguments(arguments)

    # else

    global WHAT_TO_GET
    if options.comments:
        WHAT_TO_GET = COMMENTS
    if options.url:
        WHAT_TO_GET = URL

    json_text = get_json_text()
    decoded = json.loads(json_text)
    process_posts(decoded)


if __name__=='__main__':
    main()

