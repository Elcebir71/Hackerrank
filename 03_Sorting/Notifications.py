#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    count, k = 0, []
    ase = defaultdict(int)
    k = expenditure
    m = k[:d].copy()
    m.sort()
    ind = d // 2
    for key,val in enumerate(k[:d]):
        ase[val] += 1

    ase = {k: v for k, v in sorted(ase.items(), key=lambda x: x[0])}
    s = 0
    down, up = d//2-9, d//2
    sum_cum = [x[0] for x in ase.items() if down <= (s := s+x[1]) <= up]

    if d % 2 != 0:
        for indx, arr in enumerate(expenditure[d:]):
            if 0 <= 2 * m[ind] <= arr:
                count += 1
                m.pop(m.index(k[indx]))
                ordinary_sort(k, m, arr)
            else:
                m.pop(m.index(k[indx]))
                ordinary_sort(k, m, arr)
    else:
        for indx, arr in enumerate(expenditure[d:]):

            if 0 <= m[ind] + m[ind - 1] <= arr:
                count += 1
                print(indx, m.index(k[indx]))
                m.pop(m.index(k[indx]))
                ordinary_sort(k, m, arr)
            else:
                print(indx, m.index(k[indx]))
                m.pop(m.index(k[indx]))
                ordinary_sort(k, m, arr)
    print(count)

    return count


def ordinary_sort(lst, srt, element):
    if element >= srt[-1]:
        srt.append(element)
    elif element <= srt[0]:
        srt.insert(0, element)
    elif element in srt:
        srt.insert(srt.index(element), element)
    else:
        start, lng = 0, len(srt)
        steps = 1 if len(srt) < 1000 else int(round(len(srt) / 10, -2))
        if srt.index(element) - lng // 2 <= 0:
            while any([element - x <= 0 for x in srt[start:lng + 1:steps]]):
                indis = [x for x in range(start, lng + 1, steps)]
                indis_boolean = [element - x <= 0 for x in srt[start:lng + 1:steps]]
                start, lng = indis[indis_boolean.index(True) - 1], indis[indis_boolean.index(True)]
                steps = int(round((lng - start) / 10, -2))

                if steps <= 10:
                    srt.insert(start + [element - x <= 0 for x in srt[start:lng + 1]].index(True), element)
                    break
        else:
            start, lng = len(srt), 0
            while any([element - x <= 0 for x in srt[start:lng - 1:-steps]]):
                indis = [x for x in range(start, lng - 1, -steps)]
                indis_boolean = [element - x <= 0 for x in srt[start:lng - 1:-steps]]
                print(indis, '\n', indis_boolean)
                start, lng = indis[indis_boolean.index(False) - 1], indis[indis_boolean.index(False)]
                steps = int(round((start - lng) / 10, -2))

                if steps <= 10:
                    srt.insert(lng + [element - x <= 0 for x in srt[lng:start + 1]].index(False), element)
                    break
    return srt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
