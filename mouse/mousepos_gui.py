#!/usr/bin/env python

"""
Monitor the mouse position.

NEW
=== 

A new coordinate system can be defined in settings.json. 
Then the script shows the absolute position (from the top left
corner), and the relative position too (from the new coordinate 
system).
"""

import sys
import os

from time import sleep

import gtk
gtk.gdk.threads_init() #@UndefinedVariable

import threading

# uses the package python-xlib
# from http://snipplr.com/view/19188/mouseposition-on-linux-via-xlib/
# or: sudo apt-get install python-xlib
from Xlib import display

# By default, the position (0,0) is in the top left corner.
# However, you might want to re-position the coordinate
# system to somewhere else. X_0 and Y_0 marks the point (0,0) 
# of this relative coordinate system.
import json
X_0 = 0  # to be read from settings.json
Y_0 = 0  # to be read from settings.json


def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    # this prints the string Xlib.protocol.request.QueryExtension to stdout,
    # that's why stdout is redirected temporarily to /dev/null
    data = display.Display().screen().root.query_pointer()._data
    sys.stdout = old_stdout
    
    return data["root_x"], data["root_y"]


class MouseThread(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self.parent = parent
        self.killed = False

    def run(self):
        try:
            while True:
                if self.stopped():
                    break
                x, y = mousepos()
                text = "Abs: {0}".format((x,y))
                title = "A: {0}".format((x,y))
                if X_0 and Y_0:
                    text += " " * 15 + "Rel: {0}".format((x-X_0, y-Y_0))
                    title += " | R: {0}".format((x-X_0, y-Y_0))
                self.parent.label.set_text(text)
                self.parent.set_title(title)
                sleep(0.5)
        except (KeyboardInterrupt, SystemExit):
            sys.exit()

    def kill(self):
        self.killed = True

    def stopped(self):
        return self.killed


class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()
        
        #self.set_title("Mouse coordinates 0.1")
        self.set_keep_above(True)   # always on top
        self.set_size_request(300, 45)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", self.quit)

        self.label = gtk.Label()

        self.mouseThread = MouseThread(self)
        self.mouseThread.start()

        fixed = gtk.Fixed()
        fixed.put(self.label, 10, 10)

        self.add(fixed)
        self.show_all()

    def quit(self, widget): #@ReservedAssignment
        self.mouseThread.kill()
        gtk.main_quit()


def read_settings():
    global X_0, Y_0
    settings = None #@UnusedVariable
    try:
        with open('settings.json') as f:
            settings = json.loads(f.read())
        if settings.has_key('x_0') and settings.has_key('y_0'): 
            X_0 = settings['x_0']
            Y_0 = settings['y_0']
    except IOError:
        print >>sys.stderr, 'Warning: settings.json is missing.'
    except ValueError:
        print >>sys.stderr, "Warning: couldn't decode settings.json"
    #
    print '# X_0:', X_0
    print '# Y_0:', Y_0

###################################################################################################

if __name__ == '__main__':
    read_settings()
    #
    app = PyApp()
    gtk.main()
