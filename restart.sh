#!/usr/bin/env bash

set -x
set -e

pushd ~/bimba

git reset --hard
git pull --rebase
# pip install -r requirements.txt
./db1000n.py

popd
