#!/usr/bin/env bash

# fftabs is a symbolic link that points to fftabs.py
# palemoon is an extremely fast web browser, based on firefox

URL=`fftabs --current`
palemoon "$URL" &
