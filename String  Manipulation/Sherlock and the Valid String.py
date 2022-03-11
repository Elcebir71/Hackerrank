#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    st = Counter(s)
    d = Counter(st.values())
    lng, sm = d.__len__(), sum(st.values())
    keys = list(d.keys())

    if lng == 1:
        print('YES')
        return 'YES'
    elif lng > 2:
        print('NO')
        return 'NO'
    else:
        if abs(keys[0] - keys[1]) == 1 and d[max(keys)] == 1:
            print('YES')
            return 'YES'
        elif d[1] == 1:
            print('YES')
            return 'YES'
        else:
            print('NO')
            return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    # fptr.write(result + '\n')

    # fptr.close()
