import math
import operator
import os
import random
import re
import sys
import time

# Complete the minimumSwaps function below.
from typing import List, Any


def minimumSwaps(arr):
    # strt = time.time()
    arrange = [x + 1 for x in range(len(arr))]
    # finish = time.time()
    # print(finish - strt)
    # strt = time.time()
    diff = [(x - y) for x, y in zip(arrange, arr)]
    # finish = time.time()
    # print(finish - strt)
    # strt = time.time()
    # index = [arr.index(x) for x in arrange]
    # finish = time.time()
    # print(finish - strt)
    # strt = time.time()
    asd = {x: y for (y, x) in enumerate(arr)}
    dict1 = dict(sorted(asd.items()))
    # finish = time.time()
    # print(finish - strt)
    cnt = 0

    # while any(diff):
    #     for i in arrange:
    #         b, a = i - 1, dict1[i]  # arr.index(i)
    #
    #         if a != b:
    #             dict1[i], dict1[arr[b]] = b, dict1[i]
    #             arr[a], arr[b] = arr[b], arr[a]
    #             cnt += 1
    #             diff = [(x - y) for x, y in zip(arrange[min(a, b):], arr[min(a, b):])]
    #         else:
    #             continue
    for i in arrange:
        b, a = i - 1, dict1[i]  # arr.index(i)

        if a != b:
            dict1[i], dict1[arr[b]] = b, dict1[i]
            arr[a], arr[b] = arr[b], arr[a]
            cnt += 1
            # diff = [(x - y) for x, y in zip(arrange[min(a, b):], arr[min(a, b):])]
        else:
            continue
    return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    strt = time.process_time_ns()
    res = minimumSwaps(arr)
    finish = time.process_time_ns()
    print(res)
    print((finish - strt) / 1000000000)

    # fptr.write(str(res) + '\n')

    # fptr.close()
