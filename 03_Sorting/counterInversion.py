import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countInversions(arr):

    return merge_sort(arr)[0]

def merge_sort(arr):
    if len(arr) > 1:
        hlf, swap = len(arr) // 2, 0
        swap_l, L = merge_sort(arr[:hlf])
        swap_r, R = merge_sort(arr[hlf:])
        swap_m, result = merge(L, R)
        return swap_m + swap_l + swap_r, result
    return 0, arr



def merge(arr1, arr2):
    temp, swap, i, j, m, n = [], 0, 0, 0, len(arr1), len(arr2)
    L, R = arr1, arr2
    app = temp.append
    while i < m and j < n:
        if L[i] <= R[j]:
            app(L[i])
            i += 1
        else:
            app(R[j])
            j += 1
            swap += m - i
            # print(swap)
        temp += L[i:]
        temp += R[j:]
    return swap, temp


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)
        print(result)

        # fptr.write(str(result) + '\n')
