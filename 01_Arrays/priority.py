#!/bin/python3

import math
import os
import random
import re
import sys
import time


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(arr) -> None:
    arr = tuple(arr)
    print(len(arr))
    new = sorted(list(set(arr)))
    diff = [x - y for x, y in zip(new, arr)]
    if not any(n < -2 for n in diff):
        strt = time.time()
        count, l, start, top = 0, [], 0, 0
        for i in diff:
            count += i
            top += 1
            if count == 0 and top - start >= 2:
                if start == 0:
                    a = [i for i in q[start:top]]
                    l.append(a)
                    start, count = top, 0
                else:
                    a = [i for i in q[start:top]]
                    l.append(a)
                    start, count = top, 0
        cnt = 0
        del new, count, start, top
        for arry in l:
            arrng = sorted(list(set(arry)))
            for k, v in enumerate(arrng):
                if v != arry[k]:
                    ind = arry.index(v)
                    cnt += ind - k
                    arry.insert(k, arry.pop(ind))
        finish = time.time()
        print()
        print(cnt, finish - strt)
    else:
        print("Too chaotic")


if __name__ == '__main__':
    t = int(input().strip())
    # q = [1, 2, 3, 5, 4, 6, 7, 8]

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))
        # q = [1, 2, 3, 5, 4, 6, 7, 8]
        minimumBribes(q)
