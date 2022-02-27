import math
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    start1 = time.process_time()
    count, med, s, counter = 0, d // 2, 0, defaultdict(int)
    rng = set(expenditure[:d])
    counter = defaultdict(int, {x: expenditure[:d].count(x) for x in rng})
    count_ord = {key: (s := s + val) for key, val in counter.items()}

    if d % 2 == 0:
        for index, arg in enumerate(expenditure[d:]):
            med_dn = next([x, y] for x, y in reversed(count_ord.items()) if y <= med)
            med_up = next([x, y] for x, y in count_ord.items() if y > med)
            pop1 = expenditure[index]
            if med_dn[1] < med:
                med1 = med2 = med_up[0]
            else:
                med1, med2 = med_dn[0], med_up[0]
            if med1 + med2 <= arg:
                count += 1
            counter[pop1] -= 1
            counter[arg] += 1
            s = 0
            count_ord = {key: (s := s + val) for key, val in counter.items()}
    else:
        md = []

        for index, arg in enumerate(expenditure[d:]):
            med_dn = next([x, y] for x, y in reversed(count_ord.items()) if y < med+1)
            med_up = next([x, y] for x, y in count_ord.items() if y >= med+1)
            pop1 = expenditure[index]
            if med_dn[1] <= med + 1:
                med1 = med_up[0]
            if 2 * med1 <= arg:
                count += 1
            counter[pop1] -= 1
            counter[arg] += 1
            s = 0
            count_ord = {key: (s := s + val) for key, val in counter.items()}

    finish = time.process_time()
    tm = (finish - start1)
    print(count, tm)
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    # fptr.write(str(result) + '\n')

    # fptr.close()
