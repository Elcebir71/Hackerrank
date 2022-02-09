# import time
from operator import add


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # q, k = [(x[0], x[1]) for x in queries], [x[2] for x in queries]
    que = sorted(queries, key=lambda x: x[0])
    array, temp = [[1, n, 0]], [[1, n, 0]]

    for q in que:
        start = [x[0] for x in temp] + [q[0]]
        end = sorted([x[1] for x in temp] + [q[1]])
        rslt = range(sorted(list(max(start), min(end))))
        srtdlst = sorted(list(set(start + end)))
        intrval = list(zip(srtdlst[:-1], srtdlst[1:]))
        for elem in intrval:
            if elem[0] == rslt.start and elem[1] == rslt.stop:
                array.append([elem[0], elem[1], temp[0][2] + q[2]])
            else:
                if intrval.index(elem) != 0:
                    array.append([elem[0]+1, elem[1], temp[0][2]])

        if len(array) >= 2:
            array.pop(0)
            # if indj != len(temp)-1 or len(temp) == 1:
            #     rslt = range(max(q[0], temp[j][0]), min(q[1], temp[j][1]))
            #     a = sorted(list(set([temp[j][0], q[0], temp[j][1], q[1]])))
            #     b = list(zip(a[:-1], a[1:]))
            #     if max(q[0], temp[j][0]) < min(q[1], temp[j][1]):
            #         for ind in range(len(b)):
            #             if b[ind][0] == rslt.start and b[ind][1] == rslt.stop:
            #                 array1.insert(indj + ind, [b[ind][0], b[ind][1], temp[j][2] + q[2]])
            #             else:
            #                 if ind == 0:
            #                     array1.insert(indj + ind, [b[ind][0], b[ind][1]-1, temp[j][2]])
            #                 else:
            #                     array1.insert(indj + ind, [b[ind][0] + 1, b[ind][1], last+q[2]])
            # else:
            #     temp[j][0] = array1[-1][1] + 1
            #     a = sorted(list(set([temp[j][0], q[0], temp[j][1], q[1]])))
            #     b = list(zip(a[:-1], a[1:]))
            #     if max(q[0], temp[j][0]) < min(q[1], temp[j][1]):
            #         for ind in range(len(b)):
            #             if b[ind][0] == rslt.start and b[ind][1] == rslt.stop:
            #                 array1.insert(indj + ind, [b[ind][0], b[ind][1], temp[j][2] + q[2]])
            #             else:
            #                 if ind == 0:
            #                     array1.insert(indj + ind, [b[ind][0], b[ind][1] - 1, temp[j][2]])
            #                 else:
            #                     array1.insert(indj + ind, [b[ind][0] + 1, b[ind][1], last])
            temp = array.copy()

        # array1 = []
    print(max(temp))
    return max(temp)


if __name__ == '__main__':
    # os.environ['OUTPUT_PATH'] = 'junk.txt'
    # fptr = open('junk.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
