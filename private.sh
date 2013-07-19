#!/bin/bash

TMP=$(mktemp)
echo $TMP
rm $TMP
git clone https://github.com/ahdinosaur/cloyne-network-private.git $TMP
cp -R $TMP/* .
rm -rf $TMP
