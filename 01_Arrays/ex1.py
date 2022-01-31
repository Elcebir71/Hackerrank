#!/bin/python3


#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    s = []
    ls = [1, 1, 1, 0, 1, 0, 1, 1, 1]
    for m in range(4):
        for k in range(4):
            new = []
            for i in range(3):
                for j in range(3):
                    new.append(arr[k+i][m+j])
            print(new)
            s.append(sum((new[x]*ls[x]) for x in range(len(ls))))
    return max(s)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

 #   for _ in range(6):
  #      arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
