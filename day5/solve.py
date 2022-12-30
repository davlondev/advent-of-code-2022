
# not the cleanest or most efficient solution
# but it is a solution


class Stack():
  def __init__(self, data = []):
    self.data = list(data)

  def push(self, val):
    self.data.append(val) 
  
  def push_multi(self, vals: list):
    #count = len(vals)
    for val in reversed(vals): 
      self.data.append(val)

  def pop(self):
    index = len(self.data)-1
    element = self.data[index]
    self.data = self.data[:index]
    return element

  def pop_multi(self, count) -> list:
    ret = []
    for i in range(count):
      ret.append(self.pop())
    return ret

  def show(self):
    print('<', end='')
    for i in self.data: print(f' {i}', end='')
    #print(f'      top: {self.top()}')
    print()

  def top(self, count=0):
    if len(self.data) <= 0:
      return "empty stack"

    return self.data[len(self.data)-1-count]



def prep_input(filename):
  with open(filename) as f:
    lines = f.readlines()
  lines = ''.join(lines)
  for i, a in enumerate(lines):
    print(str(i) + ':', a)
  print('-------------------------')
  return lines


# return list of stacks and list of instructions
def extract_stacks_and_instructions(inputstr) -> (list, list):
  res = []
  lines = inputstr.split('\n')
  first_line = lines[0]
  n_stacks = first_line.count('[')

  instructionlineindex = 0
  for i, line in enumerate(lines):
    if line.find('[') == -1: 
      instructionlineindex = i
      break
    line = line.replace('    ', ', ').replace('[','').replace(']','').split(',')
    #res.append(line)
    res.append(''.join(line).split(' '))
    #print(i, line)
  maxstackcount = 0
  for i, row in enumerate(res):
    print(i, row)
    if len(row) > maxstackcount: maxstackcount = len(row)

  print('-------------------------')
  print(maxstackcount, 'stacks found')
  print('-------------------------')
  print(res)

  stacks = []
  for i in range(maxstackcount): stacks.append(Stack()) 

  for i, row in enumerate(reversed(res)):
    for n, item in enumerate(row):
      if item == '': continue
      stacks[n].push(item)
    
  print()
  return (stacks, lines[instructionlineindex+2:-1])

def showstacks(stacks):
  for i, stack in enumerate(stacks):
    print('stack', i, ':', end=' ')
    stack.show()


# do instructions and return top item of each stack
def solve(stacks, instructions) -> str:
  print('MOVES')
  print('-------------------------')
  for ins in instructions:
    ins = ins.split(' ')
    itemcount = int(ins[int(ins.index('move')+1)])
    source = int(ins[int(ins.index('from')+1)])
    destination = int(ins[int(ins.index('to')+1)])
    print(ins, '----->', itemcount, source, destination, '\n')

    if itemcount == 1:
      stacks[destination-1].push(stacks[source-1].pop())

    elif itemcount > 1:
      print('multi')
      stacks[destination-1].push_multi(stacks[source-1].pop_multi(itemcount))

    showstacks(stacks)
    print('-------------------------')

  print('-------------------------')
  showstacks(stacks)
  ret = ''.join([stacks[x].top() for x in range(len(stacks))])
  print('result:', ret)
  return ret

testinput = prep_input("testinput.txt")
testinput = prep_input("input.txt")
stacks, instructions = extract_stacks_and_instructions(testinput)
showstacks(stacks)
print('-------------------------')
solve(stacks, instructions)


