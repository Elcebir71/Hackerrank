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
    # Write your code here
    res = countSwaps(arr)
    print(res)
    return res
def countSwaps(a):
    countdown, i, lng, = 0, 0, len(a)
    while i is not None and any((x - y > 0 for x, y in zip(a[i:lng - 1], a[i+1:]))):
        i = next((i for i, x, y in zip(range(lng - 1), a[:lng - 1], a[1:]) if x - y > 0), None)
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 1
        countdown += 1
    return countdown



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        #fptr.write(str(result) + '\n')

    #fptr.close()
