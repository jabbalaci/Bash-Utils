#!/usr/bin/env python2

"""
Interacting with processes.
"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import shlex
from subprocess import call, PIPE, Popen, STDOUT


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """Execute a simple external command and get its output.

    The command contains no pipes. Error messages are
    redirected to the standard output by default.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0].decode("utf8")


def execute_cmd(cmd):
    """Execute a simple external command."""
    args = shlex.split(cmd)
    call(args)
