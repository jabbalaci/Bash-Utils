#!/usr/bin/env python

"""
Monitor the mouse position.
"""

import sys
import os

from time import sleep

import gtk
gtk.gdk.threads_init()

import threading

# uses the package python-xlib
# from http://snipplr.com/view/19188/mouseposition-on-linux-via-xlib/
# or: sudo apt-get install python-xlib
from Xlib import display


old_stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')


def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
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
                text = "{0}".format(mousepos())
                self.parent.label.set_text(text)
                self.parent.set_title(text)
                sleep(0.05)
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
        self.set_size_request(250, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", self.quit)

        self.label = gtk.Label()

        self.mouseThread = MouseThread(self)
        self.mouseThread.start()

        fixed = gtk.Fixed()
        fixed.put(self.label, 10, 10)

        self.add(fixed)
        self.show_all()

    def quit(self, widget):
        self.mouseThread.kill()
        gtk.main_quit()


if __name__ == '__main__':
    app = PyApp()
    gtk.main()
