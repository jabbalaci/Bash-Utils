#!/usr/bin/env python

import os

CREDENTIALS = '{home}/secret/reddit/credentials.txt'.format(home=os.path.expanduser('~'))
LATEST_SUBREDDIT = '{home}/secret/reddit/latest_subreddit.txt'.format(home=os.path.expanduser('~'))


def read_credentials():
    f = open(CREDENTIALS, 'r')
    user = f.readline().rstrip('\n')
    passwd = f.readline().rstrip('\n')
    f.close()

    return user, passwd

USERNAME, PASSWORD = read_credentials()


def get_latest_subreddit():
    try:
        f = open(LATEST_SUBREDDIT, 'r')
        text = f.readline().rstrip('\n')
        f.close()
    except IOError:
        return ''

    return text


def set_latest_subreddit(text):
    f = open(LATEST_SUBREDDIT, 'w')
    print >>f, text
    f.close()

#############################################################################

if __name__ == "__main__":
    print USERNAME, PASSWORD
    print get_latest_subreddit()
