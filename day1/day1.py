

def solve(filename):
    with open(filename) as f:
        lines = f.readlines()
    f.close()

    maxmax = 0
    curmax = 0
    for i in lines:
        if i == '\n':
            if curmax > maxmax:
                maxmax = curmax
            curmax = 0
            continue

        curmax += int(i)
        
    print(maxmax)


solve("testinput.txt")


