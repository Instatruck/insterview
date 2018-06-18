#!/bin/bash

export DOC_FILES=instatest.py
for i in $DOC_FILES; do
    pdoc $i --html --html-dir ./docs --overwrite
done