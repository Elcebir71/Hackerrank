def sherlockAndAnagrams(s):
    anagram, res, j = [], [], 0
    empty =set()

    for i in range(len(s)):
        # Finding repeating elements, indices and counting also first occurrence
        dx = [(s[i], i, s[:i + 1].count(s[i]), i) if s[:i + 1].count(s[i]) >= 2 else (
            s[i], i, s[:i + 1].count(s[i])) for i in range(len(s))]

        dic1 = {key: [val]  for key, val in zip([item0[0] for item0 in dx], [item1[1] for item1 in dx])}
        dict1 = {key: [val] if dx[val][2] == 1 else [dx[val][3]] + [val] for key, val in
                 zip([item0[0] for item0 in dx], [item1[1] for item1 in dx])}
        # Finding the indices of repeating elements by one
        ind = [item[1] for item in dx]
        # Combination without repetition
        com = [[x, y] for x in ind for y in ind[ind.index(x):] if not x == y]

        for j in range(len(s) - j):
            x = s[j: i + j + 1]
            dictx = {a: idx for a, idx in enumerate(x)}
            if len(x) >= i + 1:
                for m in range(j + 1, len(s) - len(x) + 1):
                    strg = s[m:len(x) + m]
                    dicts = {a: strg.count(a) for a in strg}
                    if dictx == dicts and [x] not in res:
                        res += [[x, strg]]
                        # for k in dictx.keys():
                        #     if k in dicts.keys() and dictx[k] == dicts[k] and :
                        #         res += [[x, strg]]
    print(res, '\n', len(res))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

    #    fptr.write(str(result) + '\n')
