#!/usr/bin/env bash

# Some tests. Just to be sure that nothing is f* up.

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`

export PYTHONPATH=$SCRIPTPATH

OPTIONS="--continue-on-collection-errors"

py.test -vs tests/ $OPTIONS
