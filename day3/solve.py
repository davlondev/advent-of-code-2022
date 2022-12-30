


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
          
  print('sum:', priosum)







testinput = loadfile("input.txt")
#print(testinput)
solve(testinput)


print(ii('a'))
print(ii('Z'))

