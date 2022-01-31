from time import process_time_ns


def arrayManipulation(n, queries):
    que = sorted(queries, key=lambda t: t[0])
    array, temp, temp1 = [], [], [[1, n, 0]]
    indt, mx = 0, 0
    basla = process_time_ns()
    for q in que:
        a, b, k = q[0], q[1], q[2]
        temp = temp1
        for element in temp:
            c, d, e = element[0], element[1], element[2]
            x, y = max(a, c), min(b, d)
            if x <= y:
                if x > c:
                    if y == d:
                        array.extend([[x, y, e + k]])
                        mx = mx if mx > e + k else e + k
                    else:
                        array.extend([[x, y, e + k], [y + 1, d, e]])
                        mx = mx if mx > e + k else e + k
                elif x == c:
                    if y == b:
                        array.extend([[x, y, e + k], [y + 1, d, e]])
                        mx = mx if mx > e + k else e + k
                    else:
                        array.extend([[x, y, e + k]])
                        mx = mx if mx > e + k else e + k
            else:
                if b < d:
                    array.extend([element])

        if len(array) >= 2:
            temp1 = []
            indt += 1
            print(indt)
            temp1.extend(array)
            # mx += [max(w[2] for w in array)]
            array = []
    bitir = process_time_ns()
    print((bitir - basla) / 1000000000)
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

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
