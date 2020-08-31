#!/bin/bash
set -e

cd src

echo Running unittest
python3 -m unittest discover

echo Running coverage test
../scripts/test_coverage.sh

echo Running style check
cd ../scripts/
python3 pylint-check.py