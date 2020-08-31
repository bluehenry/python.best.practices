#!/usr/bin/env bash

coverage run --source="." --omit="./tests*","./main*","./config*","./dto*" -m unittest discover
report=$(coverage report)
coverage report
reportArr=(${report})

lastPos=`expr ${#reportArr[@]} - 1`
coverage=${reportArr[$lastPos]}
coverageNum=${coverage%"%"*}

passCoverageNum=80

if [[ ${coverageNum} -gt ${passCoverageNum} ]]
  then
    echo "test coverage enough, test coverage check pass"
  else
    echo "test coverage not enough, test coverage check faild"
    exit 1
fi