#!/usr/bin/bash

DIR=$1
PROBLEM=$2
URL=$3

rm -r tmp

wget -O tmp.zip ${URL}

mkdir tmp
unzip -d tmp -j tmp.zip
rm tmp.zip

mv tmp "${DIR}/${PROBLEM}_files"