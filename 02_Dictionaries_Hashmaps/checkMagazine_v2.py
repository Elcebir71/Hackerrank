from time import process_time
import yappi
def checkMagazine(magazine, note):
    count = 0


    note1 = sorted(set(note))
    magazine1 = sorted(set(magazine))
    qaw = {x: note1.count(x) for x in note1}
    ase = {x: magazine1.count(x) for x in magazine1}
    yappi.set_clock_type('cpu')
    for k, v in qaw.items():
        yappi.start()
        if qaw[k] <= ase[k]:
            count += 1
    yappi.get_func_stats().print_all()
    print(yappi.get_thread_stats())
    if count == len(qaw):
        print('Yes')
        exit()
    else:
        print('No')
        exit()

    start = 0
    # # [magazine.remove(note[i]) for i in range(len(note)) if note[i] in magazine]
    # end = process_time()
    # print(end - start)




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)