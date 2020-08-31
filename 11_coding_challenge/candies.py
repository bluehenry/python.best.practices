#!/bin/python3
# https://www.hackerrank.com/challenges/candies/problem

import os

# Complete the candies function below.
def candies(n, arr):
    candies = []

    for _ in range(n):
        candies.append(1)

    i = 0
    while i < n - 1:
        if arr[i] < arr[i+1]:
           candies[i+1] = candies[i] + 1
        i += 1

    i = n - 1
    while i > 0:
        if arr[i] < arr[i-1]:
            candies[i-1] = max(candies[i-1], candies[i]+1)
        i -= 1

    total = 0
    for i in range(len(candies)):
        total += candies[i]

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
