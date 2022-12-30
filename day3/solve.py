


alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ii = lambda a : alphabet.find(a)


def loadfile(filename):
  with open(filename) as f:
    lines = f.readlines()
  f.close()
  return lines

def solve(lines):
  priosum = 0
  for line in lines:
    l = int(len(line)/2)
    item1, item2 = line[:l], line[l:]
    print('\n\nitems:', item1, item2)
    found = False
    founditem = ''
    for i1 in item1:
      if found == True:
        break
      for i2 in item2:
        if i1 == i2:
          founditem = i1
          found = True
          priosum += ii(founditem)
          break
    print('found:', founditem)
          
  print('\n\n---------\nsum:', priosum)


def solve2(lines):
  linecount = len(lines)
  print(linecount, 'lines:')
  print(''.join(lines),end='')
  print('----------------')
  
  priosum = 0
  groupsum = 0

  curline = 0 # line index

  groupsize = 3

  while curline <= linecount - groupsize:
    line = lines[curline]
    l = len(line)

    # find common group
    line1, line2, line3 = lines[curline], lines[curline+1], lines[curline+2]
    print('\n-------\ngroups:\n', line1, line2, line3, end='\n')
    foundgroup = ''

    for i1 in line1:
      if foundgroup != '': break

      for i2 in line2:
        if foundgroup != '': break

        for i3 in line3:
          if i1 == i2 == i3:
            foundgroup = i1
            groupsum += ii(foundgroup)
            print('found group:', foundgroup, ii(foundgroup), end='\n\n')
            break
    
    curline += groupsize

  print('sum:', groupsum)
  return groupsum


print('------------------------')

testinput = loadfile("input.txt")
#print(testinput)
#solve(testinput)
solve2(testinput)



