#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sfromLeft=0
    sfromright=0

    for i in range(0,len(arr)):
        sfromLeft=sfromLeft+(arr[i][i])
        sfromright=sfromright+(arr[i][(len(arr)-i-1)])
    if(sfromright>sfromLeft):
        print(sfromright-sfromLeft)
    else:
        print(sfromLeft-sfromright)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
