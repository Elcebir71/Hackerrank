from time import process_time_ns

def arrayManipulation(n, array1):
    # que = sorted(array1, key=lambda t: t[0])
    array = [0] * n
    mx, sum = 0, 0
    for q in queries:
        a, b, k = q[0], q[1], q[2]
        array[a-1] = array[a-1] + k
        if b < n:
            array[b] = array[b] - k
    for i in range(n):
        sum += array[i]
        mx = max(sum, mx)
    return mx


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)