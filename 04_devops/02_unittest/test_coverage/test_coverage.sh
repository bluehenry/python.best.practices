#!/usr/bin/env bash

PYTHONPATH=./src coverage run --source "./src" --omit="src/__init__.py","src/settings.py" -m unittest discover

report=$(coverage report)
coverage report
reportArr=($report)

lastPos=`expr ${#reportArr[@]} - 1`
coverage=${reportArr[$lastPos]}
coverageNum=${coverage%"%"*}

passCoverageNum=80

if [ $coverageNum -gt $passCoverageNum ]
  then
    echo "Tests coverage checking passed"
  else
    echo "Tests coverage checking failed"
    exit 1
fi