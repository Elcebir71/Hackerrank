#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    countdown,array, temp, i, lng = 0, [a.copy()], [], 0, len(a)
    while (i<lng-1 and not (all(x-y == -1 for x, y in zip(a[:lng-1],a[1:])))):
        s1, s2 = a[i], a[i+1]
        if s1 - s2 > 0:
            a[i], a[i+1] = s2, s1
            countdown += 1
            # array.append([a.copy()])
        i += 1
        if (i == lng-1 and not all((x - y <= -1 for x, y in zip(a[:lng - 1], a[1:])))):
            i = [x - y <= -1 for x, y in zip(a[:lng - 1], a[1:])].index(False)
    print('Array is sorted in %d swaps.' % countdown)
    print('First Element: %d' % a[0])
    print('Last Element: %d' % a[-1])
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
