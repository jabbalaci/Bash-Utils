#!/usr/bin/env python

"""
Reddit, browse all pages of a subreddit
=======================================

Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: ...
GitHub:  https://github.com/jabbalaci/Bash-Utils

When you visit a subreddit on reddit.com, for instance
http://www.reddit.com/r/python, at the bottom of the page
you will find just a "next" link to the next page.
Needless to say, browsing older entries like that is a PITA...
This script generates a simple static HTML page with links to
all the older pages: [1] [2] [3]...

Limitation
----------

This script made me figure out that reddit lists only the last 1000
posts! Older posts are hidden. If you have a direct link to them, fine,
otherwise they are gone :(
So this script will only list 40 pages. This is a limitation of reddit.

More info:

* http://www.reddit.com/r/help/comments/jhx5p/only_1000_posts_per_subreddit/
* http://www.reddit.com/r/help/comments/jhxmr/why_are_we_limited_in_the_number_of_links_we_can/

Usage:
------------

./reddit_get_all_pages.py
"""

import sys
import urllib
import json
import webbrowser

# no trailing slash:
BASE = 'http://www.reddit.com'
# This one can be customized. No trailing slash:
REDDIT = 'http://www.reddit.com/r/python'
#REDDIT = 'http://www.reddit.com/r/nsfw'
# output file:
OUTPUT_FILE = 'out.html'

page_cnt = 1


class HtmlWriter:
    def __init__(self):
        self.file = open(OUTPUT_FILE, 'w')
        self.add_header()
        print >>self.file, "<h2>{reddit}</h2>".format(reddit=REDDIT)
        
    def close(self):
        self.add_footer()
        self.file.close()
        print >>sys.stderr, "# the output was written to {out}".format(out=OUTPUT_FILE)
        
    def add(self, page, url):
        link = '<a href="{url}">{page}</a>'.format(url=url, page=page)
        print >>self.file, "[{link}] ".format(link=link)
        
    def add_header(self):
        print >>self.file, "<html>"
        print >>self.file, "<body>"
        
    def add_footer(self):
        print >>self.file, "</body>"
        print >>self.file, "</html>"


def add_json(reddit):
    reddit = reddit.replace('/?', '/.json?')
    if '/.json' not in reddit:
        reddit = reddit + '/.json'
    return reddit


def get_json_text(reddit):
    page = reddit
    sock = urllib.urlopen(page)
    json_text = sock.read()
    return json_text


def find_all_pages(reddit):
    global page_cnt
    
    html = HtmlWriter()
    
    while True:
        json_url = add_json(reddit)
        json_text = get_json_text(json_url)
        decoded = json.loads(json_text)
        posts = decoded['data']['children']
        if len(posts) == 0:
            break
        print >>sys.stderr, "# page {cnt:03}: {reddit}".format(cnt=page_cnt, reddit=reddit)
        html.add(page_cnt, reddit)
        last_post = posts[-1]
        name = last_post['data']['name']
        reddit = "{R}/?count=25&after={name}".format(R=REDDIT, name=name)
        page_cnt += 1
        
    html.close()


def main():
    find_all_pages(REDDIT)
    webbrowser.open(OUTPUT_FILE)


if __name__=='__main__':
    main()
