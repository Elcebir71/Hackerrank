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
    global swap
    swap, temp = 0, arr.copy()
    if len(arr) > 1:
        hlf = len(arr) // 2
        L = temp[:hlf]
        R = temp[hlf:]
        countInversions(L)
        countInversions(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                temp[k] = L[i]
                i += 1
            else:
                temp[k] = R[j]
                j += 1
            k += 1
        swap += j

        while i < len(L):
            temp[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            temp[k] = R[j]
            j += 1
            k += 1

    return swap


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)
        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
