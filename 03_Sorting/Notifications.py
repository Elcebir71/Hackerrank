#!/bin/python3

import math
import os
import random
import re
import sys


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
    print(ind)
    if d % 2 != 0:
        for indx, arr in enumerate(expenditure[d:]):

            if 0 < 2 * k[ind] <= arr:
                count += 1
                k.pop(0)
                ordinary_sort(k, arr)
            else:
                k.pop(0)
                ordinary_sort(k, arr)
    else:
        for indx, arr in enumerate(expenditure[d:]):

            if 0 <= k[ind] + k[ind - 1] <= arr:
                count += 1
                k.pop(0)
                ordinary_sort(k, arr)
            else:
                k.pop(0)

                ordinary_sort(k, arr)
    print(count)
    print(k[-1])
    return count


def ordinary_sort(lst, element):
    if element >= lst[-1]:
        lst.append(element)
    elif element <= lst[0]:
        lst.insert(0, element)
    else:
        start,  lng = 0, len(lst)
        lng = len(lst) if len(lst) < 1000 else int(round(lng, -2)) + 1
        steps = 1 if lng < 1000 else int(round(len(lst) / 10, -2))
        while any([element - x <= 0 for x in lst[start:lng:steps]]):
            indis = [x for x in range(start, lng, steps)]
            indis_boolean = [element - x <= 0 for x in lst[start:lng:steps]]
            start, lng = indis[indis_boolean.index(True) - 1], indis[indis_boolean.index(True)]
            steps = int(round((lng - start) / 10, -2))
            if steps <= 100:
                lst.insert(start + [element - x <= 0 for x in lst[start:lng+1]].index(True), element)
                break
    return lst


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
