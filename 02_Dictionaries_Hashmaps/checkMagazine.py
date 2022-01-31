
def checkMagazine(magazine, note):
    # This version is working checking existence of string to write a ransom code
    # str1 = ' '.join(map(str, sorted(magazine)))
    # str2 = ' '.join(map(str, sorted(note)))
    # s = set()
    count = 0


    # asw = [x for x in note if x in s or (s.add(x) or False)]
    # repeat = [word for word in magazine if word in note]
    set_note = set(note)
    if len(set_note) == len(note):
        if all([str in magazine for str in note]):
            print('Yes')
            exit()
        else:
            print('No')
            exit()
    else:
        q = set()
        duplicated_items = list(set(x for x in note if x in q or (q.add(x) or False)))
        for i in range(len(duplicated_items)):
            if magazine.count(duplicated_items[i]) >= note.count(duplicated_items[i]) :
                count += 1
        if count == len(duplicated_items) and all([string in magazine for string in note]):
            print('Yes')
            exit()
        else:
            print('No')
            exit()













if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)