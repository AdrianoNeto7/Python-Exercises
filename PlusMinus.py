#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    countPositive = 0
    countNegative = 0
    countZero = 0
    ratioPositive = 0.000000
    ratioNegative = 0.000000
    ratioZero = 0.000000
    for i in arr:
        if i > 0:
            countPositive = countPositive + 1
        elif i < 0:
            countNegative = countNegative + 1
        else:
            countZero = countZero + 1

    #calculating the ratios
    ratioPositive = countPositive / n
    ratioNegative = countNegative / n
    ratioZero = countZero / n

    #Printing the ratios
    print(str(ratioPositive) + "\n" + str(ratioNegative) + "\n" + str(ratioZero))    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)