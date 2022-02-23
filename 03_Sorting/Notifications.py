#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    count, last, sum_lst, k = 0, 0, 0, []
    k = [i for i in expenditure[:d]]
    k.sort()
    ind = d // 2
    if d % 2 != 0:
        for indx, arr in enumerate(expenditure[d:]):
            if 0 < 2 * k[ind] <= arr:
                count += 1
                k.pop(0)
                ordinarySort(k, arr)
            else:
                k.pop(0)
                ordinarySort(k, arr)
    else:
        for indx, arr in enumerate(expenditure[d:]):
            if 0 <= k[ind] + k[ind + 1] <= arr:
                count += 1
                k.pop(0)
                ordinarySort(k, arr)
            else:
                k.pop(0)
                ordinarySort(k, arr)
    return count

def ordinarySort(lst, element):
    if element >= lst[-1]:
        lst.append(element)
    elif element <= lst[0]:
        lst.insert(0, element)
    else:
        m, times = len(lst), 0
        indis, half = [m // 2], m // 2
        if element - lst[indis[0]] > 0:
            while element - lst[indis[-1]] > 0:
                half = half // 2
                if indis[-1] + half <= m:
                    indis.append(indis[-1] + half)
                else:
                    break
            if indis[-1] - indis[-2] > 1:
                last1 = [ind2 for ind2, x in enumerate(lst[indis[-2]:indis[-1]]) if x <= element]

                lst.insert(indis[-2] + last1[-1] + 1, element)
            else:
                lst.insert(indis[-1] + 1, element)
        else:
            while element - lst[indis[-1]] <= 0:
                indis.append(indis[-1] // 2)
            if indis[-2] - indis[-1] > 1:
                last1 = [ind2 for ind2, x in enumerate(lst[indis[-1]:indis[-2]]) if x >= element]

                lst.insert(indis[-1] + last1[-1] + 1, element)
            else:
                lst.insert(indis[-1] + 1, element)

    return lst


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')

    #fptr.close()
