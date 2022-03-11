import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the substrCount function below.
def substrCount(n, s):
    cnt = n
    for i in range(n):
        j = i
        while j < n - 1:
            j += 1
            if s[j] == s[i]:
                cnt += 1
            else:
                if s[i:j] == s[j + 1 : 2 * j - i + 1]:
                    cnt += 1
                break

    return cnt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
