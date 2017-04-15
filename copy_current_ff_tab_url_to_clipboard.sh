#!/usr/bin/env bash

# fftabs is a symbolic link that points to fftabs.py

URL=`fftabs --current`
echo "$URL" | tocb
