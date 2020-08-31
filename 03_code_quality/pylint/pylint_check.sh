#!/usr/bin/env bash

pylint ./src
report=$(pylint src)
echo $report
result=$(echo $report | grep "Module")

if [[ "$result" != "" ]]
then
    echo "pylint checking failed"
    exit 1
else
    echo "pylint checking passed"
fi