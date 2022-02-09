from functools import reduce
def sherlockAndAnagrams(s):
    set_rptng = set(s)
    lngth_s = len(s)
    lngth_r = len(set_rptng)
    res, j = [], 0
    if lngth_s != lngth_r:
        key_val = {}
        for index, char in enumerate(s):
            if char not in key_val:
                key_val[char] = [index]
            else:
                key_val.update({char: key_val[char]+[index]})
        indices = [item for item in key_val.values() if len(item) > 1]
        for i in range(lngth_s - 1):
            if i == 0:
                for item in indices:
                    for x in item[:-1]:
                        for y in item[1:]:
                            if not x == y and y > x:
                                res.append([s[x], s[y]])
            else:
                subx = [s[j: j+i + 1:] for j in range(lngth_s-i-1)]
                subs = [s[j+1: j+i + 2:] for j in range(lngth_s-i) if len(s[j+1: j+i + 2:]) >= i + 1]
                for inx, x in enumerate(subx):
                    dictx = {a: x.count(a) for a in x}
                    for sub in subs[inx:]:
                        if x[0] in sub:
                            dicts = {a: sub.count(a) for a in sub}
                            if dictx == dicts and [x] not in res:
                                res += [[x, sub]]


    print(len(res))
    print(res)








if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

    #    fptr.write(str(result) + '\n')