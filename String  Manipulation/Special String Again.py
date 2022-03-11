import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the substrCount function below.
def substrCount(n, s):
    strng = defaultdict(list)
    for ind, char in enumerate(s):
        strng[char] += [ind]
    sub = 'aa'
    sum(1 for _ in s.startwith(sub))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
