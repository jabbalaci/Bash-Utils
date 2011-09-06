#!/usr/bin/env python

"""
Extract Firefox cookies
=======================

This script extracts cookies from Firefox's cookies.sqlite file
that are specific to a given host. The exported cookies are saved
in the file cookies.txt.

Then, you can use this exported file with wget to download content
that require authentication via cookies:

wget --cookies=on --load-cookies=cookies.txt --keep-session-cookies "http://..."

The original script was written by Dirk Sohler:
https://old.0x7be.de/2008/06/19/firefox-3-und-cookiestxt/

This version is a bit refactored but does exactly the same.
Website: https://ubuntuincident.wordpress.com/2011/09/05/download-pages-with-wget-that-are-protected-by-cookies/
GitHub:  https://github.com/jabbalaci/Bash-Utils (see the firefox/ folder)
"""
 
import os
import sys
import sqlite3 as db

USERDIR = 'w3z7c6j4.default'

COOKIEDB = os.path.expanduser('~') + '/.mozilla/firefox/' + USERDIR + '/cookies.sqlite'
OUTPUT = 'cookies.txt'
CONTENTS = "host, path, isSecure, expiry, name, value"


def extract(host):
    conn = db.connect(COOKIEDB)
    cursor = conn.cursor()
         
    sql = "SELECT {c} FROM moz_cookies WHERE host LIKE '%{h}%'".format(c=CONTENTS, h=host)
    cursor.execute(sql)
     
    out = open(OUTPUT, 'w')
    cnt = 0
    for row in cursor.fetchall():
        s = "{0}\tTRUE\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(row[0], row[1],
                 str(bool(row[2])).upper(), row[3], str(row[4]), str(row[5]))
        out.write(s)
        cnt += 1
     
    print "Gesucht nach: {0}".format(host)
    print "Exportiert: {0}".format(cnt)
     
    out.close()
    conn.close()

    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "{0}: error: specify the host.".format(sys.argv[0])
        sys.exit()
    else:
        extract(sys.argv[1])
