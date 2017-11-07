#!/usr/bin/env bash
##
# Set up symlinks for econplayground.js development
#

DEST_DIR="media/econplayground.js/"
ORIG_DIR="$HOME/public_html/econplayground.js/build/static/js/"

rm $DEST_DIR/*.js

ln -s $ORIG_DIR/main.js $DEST_DIR/main.js
ln -s $ORIG_DIR/viewer.js $DEST_DIR/viewer.js