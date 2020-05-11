#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
from collections import Counter
def birthdayCakeCandles(ar):
    print( ar.count(max(ar)))
    maxi=max(ar)
    dic=Counter(ar)
    return (dic.get(maxi))
    # print(dic.get(maxi))
    # print(maxi)
    # print(dic)

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)


