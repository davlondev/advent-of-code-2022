

#     A   :   rock      :   1
#     B   :   paper     :   2
#     C   :   scissors  :   3

#     X   :   rock
#     Y   :   paper
#     Z   :   scissors

#     loss    :    0
#     draw    :    3 
#     win     :    6

# choice + win points

# inputdata = list(str.split("\n"))

choices = {
  'A':1, 'B':2, 'C':3,
  'X':1, 'Y':2, 'Z':3,
}

outcomes = {
  'AX':3, 'AY':6, 'AZ':0,
  'BX':0, 'BY':3, 'BZ':6,
  'CX':6, 'CY':0, 'CZ':3,
}

def solve(inputdata):
  score = 0 
  for i, line in enumerate(inputdata):
    if line == '': break
    line = line.replace(' ', '')
    this_score = outcomes[line] + choices[line[1]]
    score += this_score
    print(i, '>', line, ':', this_score)
  print(score)

      

def prep_input(filename):
  with open(filename) as f:
    lines = f.readlines()
  f.close()
  lines = ''.join(lines).replace(' ', '')
  #print(lines)
  return lines.split('\n')


testinput = ("AY\nBX\nCZ").split('\n')
realinput = prep_input("input.txt")


#print(realinput)
#print()
#print(testinput)

#solve(testinput)
solve(realinput)


