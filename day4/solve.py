

def prep_input(filename):
  with open(filename) as f:
    lines = f.readlines()
  f.close()
  return [x.replace('\n', '') for x in lines]


def overlapping(p1_start: int, p1_end:int , p2_start: int, p2_end: int) -> bool:
  if p1_start >= p2_start and p1_start <= p2_end: 
    print(' : p1_start:', p1_start, 'within', p2_start, '-', p2_end)
    return True 

  if p2_start >= p1_start and p2_start <= p1_end: 
    print(' : p2_start:', p2_start, 'within', p1_start, '-', p1_end)
    return True


  if p1_start >= p2_start and p1_end <= p2_end: return True
  if p2_start >= p1_start and p2_end <= p1_end: return True
  
  return False


def solve(inputstr):
  print(inputstr)
  linecount = len(inputstr)
  groupsize = 2

  overlapsum = 0 # totally overlap

  for n, i in enumerate(inputstr):
    i1, i2 = i.split(',')[0].split('-'), i.split(',')[1].split('-')
    # if i1 inside i2
    print(n, i1, i2, end='')
    if int(i1[0]) >= int(i2[0]) and int(i1[1]) <= int(i2[1]):
      overlapsum += 1
      print(' true')
      continue
    if int(i2[0]) >= int(i1[0]) and int(i2[1]) <= int(i1[1]):
      overlapsum += 1
      print(' true')
      continue
    print(' false')

  print('sum:', overlapsum)
  return overlapsum


def solve2(inputstr):

  print(inputstr)
  linecount = len(inputstr)
  groupsize = 2

  overlapsum = 0 # partially overlap

  for n, i in enumerate(inputstr):
    i1, i2 = i.split(',')[0].split('-'), i.split(',')[1].split('-')
    print(n, i1, i2, end='')
    if overlapping(int(i1[0]), int(i1[1]), int(i2[0]), int(i2[1])):
      overlapsum += 1
      #print(' : true')
      continue
    print(' : false')

  print('sum:', overlapsum)
  return overlapsum



testinput = prep_input('testinput.txt')
realinput = prep_input('input.txt')

#solve2(testinput)
solve2(realinput)

