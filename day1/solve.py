

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


def solve2(filename):
    with open(filename) as f:
        lines = f.readlines()
    f.close()

    maxs = [0,0,0]
    curmax = 0
    for i in lines:
        if i == '\n':
            maxs = sorted(maxs) 
            #print(curmax)
            #print(maxs)
            for x in range(len(maxs)):
                if curmax > maxs[x]:
                    maxs[x] = curmax
                    break
            curmax = 0
            continue

        curmax += int(i) 

    print(maxs, sum(maxs))

#solve("testinput.txt")
solve2("input.txt")


