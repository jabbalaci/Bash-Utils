#!/usr/bin/env python

"""
"""

import sys
import urllib
import json
import webbrowser
import operator
import time

# no trailing slash:
BASE = 'http://www.reddit.com'
# This one can be customized. No trailing slash:
REDDIT = 'http://www.reddit.com/r/python'
# output file:
OUTPUT_FILE = 'out.html'

BODY_BGCOLOR = '#EAF1FD'

LIMIT_PAGES = 1
LIMIT_TOP = None


class HtmlWriter:
    def __init__(self):
        self.old_stdout = sys.stdout
        self.f = open(OUTPUT_FILE, 'w')
        sys.stdout = self.f

        self.add_header()
        print "<h2>{reddit}</h2>".format(reddit=REDDIT)

    def process(self, posts):
        self.open_table()
        print """
<th>Index</th>
<th>#&nbsp;votes</th>
<th>#&nbsp;comments</th>
<th>Title</th>
<th>Date (yyyy.mm.dd.)</th>
"""
        global LIMIT_TOP
        if not LIMIT_TOP:
            LIMIT_TOP = len(posts.posts)

        for index, p in enumerate(posts.posts[:LIMIT_TOP]):
            pos = index + 1
            print '<tr>'
            print '<td><center>{pos}</center></td>'.format(pos=pos)
            print '<td><center><b>{score}</b></center></td>'.format(score=p.score)
            print '<td><center>{comments}</center></td>'.format(comments=p.comments_num)
            print '<td><a href="{url}">{title}</a></td>'.format(title=p.title, url=p.comments_url)
            print '<td>{date}</td>'.format(date=p.date_str())
            print '</tr>'
        self.close_table()
        self.close()

    def open_table(self):
        print '<table border="1" cellpadding="5">'

    def close_table(self):
        print '</table>'

    def close(self):
        self.add_footer()

        self.f.close()
        sys.stdout = self.old_stdout
        print >>sys.stderr, "# the output was written to {out}".format(out=OUTPUT_FILE)

    def add(self, page, url):
        link = '<a href="{url}">{page}</a>'.format(url=url, page=page)
        print "[{link}] ".format(link=link)

    def add_header(self):
        print """<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
</head>
<body bgcolor="{c}">""".format(c=BODY_BGCOLOR)

    def add_footer(self):
        print "</body>"
        print "</html>"


class Posts:
    def __init__(self):
        self.posts = []

    def add(self, post):
        self.posts.append(post)

    def sort(self):
        self.posts.sort(key=operator.attrgetter("score"), reverse=True)

    def show(self):
        for post in self.posts[:LIMIT_TOP]:
            print post


class Post:
    def __init__(self, post):
        post = post['data']
        #self.score = post['score']     # minimum: 0
        self.score = post['ups'] - post['downs']    # this can go below 0 :)
        self.title = post['title'].encode('utf-8')
        self.comments_url = '{R}{url}'.format(R=BASE, url=post['permalink'].encode('utf-8'))
        self.secs = post['created']
        self.comments_num = post['num_comments']

    def __str__(self):
        sb = []
        sb.append('({score}) '.format(score=self.score))
        sb.append('[{title}]({url})'.format(title=self.title, url=self.comments_url))
        return ''.join(sb)

    def date_str(self):
        stime = time.gmtime(self.secs)
        return '{y}.{m:02d}.{d:02d}.'.format(y=stime[0], m=stime[1], d=stime[2])


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


def traverse_pages(reddit, posts):
    page_cnt = 1

    while True:
        if LIMIT_PAGES and page_cnt > LIMIT_PAGES:
            break
        # else
        json_url = add_json(reddit)
        json_text = get_json_text(json_url)
        decoded = json.loads(json_text)
        children = decoded['data']['children']
        if len(children) == 0:
            break
        print >>sys.stderr, "# page {cnt:03}: {reddit}".format(cnt=page_cnt, reddit=reddit)
        for child in children:
            post = Post(child)
            posts.add(post)
        last_post = children[-1]
        name = last_post['data']['name']
        reddit = "{R}/?count=25&after={name}".format(R=REDDIT, name=name)
        page_cnt += 1

    return posts


def main():
    posts = Posts()
    html = HtmlWriter()

    posts = traverse_pages(REDDIT, posts)

    posts.sort()
    html.process(posts)
    #posts.show()
    webbrowser.open(OUTPUT_FILE)


if __name__ == '__main__':
    main()
