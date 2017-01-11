#!/usr/bin/env python3

"""Firefox Tabs.

Usage:
  fftabs.py -a | --all
  fftabs.py -u | --url
  fftabs.py -l | --list
  fftabs.py -t | --title
  fftabs.py (-f | --focus) ID
  fftabs.py --count
  fftabs.py (-c | -k | --close) ID...
  fftabs.py -r | --raw
  fftabs.py -h | --help
  fftabs.py -V | --version

Options:
  -a --all          List all tabs in a readable format.
  -u --url          Show URLs.
  -l --list         URL lister.
  -t --title        Show titles.
  -f --focus        Focus on selected tab, where ID is the tab index.
  --count           Number of tabs.
  -c -k --close     Close (kill) selected tab, where ID is the tab index(es).
  -r --raw          List all tabs in raw format.
  -h --help         Show this screen.
  -V --version      Show version.
"""

from docopt import docopt

from lib import firefox as ff

__project__ = 'Firefox Tabs'
__version__ = '0.1'


INFO = """
A command line program for manipulating Firefox tabs.

Requirements:
* Firefox
* MozRepl add-on (https://addons.mozilla.org/en-US/firefox/addon/mozrepl/)
  - activate the add-on (under Tools -> MozRepl, "Start" and "Activate on startup")
"""


def option_raw():
    for e in ff.get_tab_list():
        print(e)


def option_all():
    li = ff.get_tab_list()
    width = len(str(len(li)))
    for d in li:
        print("{index}: {url} ({title})".format(index=str(d['index']).rjust(width),
                                                url=d['url'],
                                                title=d['title']))

def option_url():
    li = ff.get_tab_list()
    width = len(str(len(li)))
    for d in li:
        print("{index}: {url}".format(index=str(d['index']).rjust(width),
                                      url=d['url']))


def option_list():
    li = ff.get_tab_list()
    for d in li:
        print(d['url'])


def option_title():
    li = ff.get_tab_list()
    width = len(str(len(li)))
    for d in li:
        print("{index}: {title}".format(index=str(d['index']).rjust(width),
                                        title=d['title']))


def option_focus(args):
    n = int(args['ID'][0])
    ff.put_focus_on_tab(n)


def option_count():
    print(ff.get_number_of_tabs())


def option_close(args):
    total = ff.get_number_of_tabs()
    li = sorted([int(x) for x in args['ID'] if 0 <= int(x) < total])
    for pos, val in enumerate(li):
        # once a tab is closed, subsequent tabs are shifted one position to the left
        ff.put_focus_on_tab(val - pos)
        print('# closing {url} ({title})'.format(url=ff.get_curr_tab_url(),
                                                 title=ff.get_curr_tab_title()))
        ff.close_curr_tab()


def main(args):
    if args['--raw']:
        option_raw()
    elif args['--all']:
        option_all()
    elif args['--list']:
        option_list()
    elif args['--url']:
        option_url()
    elif args['--title']:
        option_title()
    elif args['--focus']:
        option_focus(args)
    elif args['--count']:
        option_count()
    elif args['--close']:
        option_close(args)
    else:
        print('# debug mode')
        print(args)

#############################################################################

if __name__ == "__main__":
    arguments = docopt(__doc__, version='{n} {v}'.format(n=__project__,
                                                         v=__version__))
    main(arguments)
