
def twoStrings(s1, s2):
    # Write your code here
    intersection = set(s1).intersection(set(s2))
    if len(intersection) > 0:
        return 'YES'

    else:
        return 'NO'


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

    #    fptr.write(result + '\n')

    #fptr.close()