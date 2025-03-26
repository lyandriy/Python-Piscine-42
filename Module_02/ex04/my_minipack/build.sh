#!/bin/bash

# Exit on error
set -e

python3 -m pip install --upgrade pip

python3 -m pip install --upgrade setuptools wheel build

rm -rf dist build *.egg-info

python3 -m build