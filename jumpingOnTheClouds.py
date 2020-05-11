#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    i = 0
    while (i < len(c)-1):
        if ((i + 2 == len(c)) or (c[i + 2] == 1)):
            i = i + 1
            jump = jump + 1
        else:
            i = i + 2
            jump = jump + 1
    print(jump)


if __name__ == '__main__':
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)



# cloud=[0, 1, 0, 0, 0, 1, 0]
# cloud1=[0,0,1,0,0,1,0]
#
# path=[]
#
# def jumpOntheClouds(cloud):
#     global path
#     i=0
#     jump=0
#     while(i<len(cloud)-1):
#         if i+2==len(cloud)or cloud[i+2]==1:
#             i=i+1
#             jump=jump+1
#         else:
#             i=i+2
#             jump=jump+1
#     print(jump)
#
#
# jumpOntheClouds(cloud1)
