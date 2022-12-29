

#     A   :   rock      :   1
#     B   :   paper     :   2
#     C   :   scissors  :   3

#     X   :   rock      :   lose
#     Y   :   paper     :   draw
#     Z   :   scissors  :   win

#     loss    :    0
#     draw    :    3 
#     win     :    6


# choice + win points

# inputdata = list(str.split("\n"))

turn_points = {
  'AA':3, 'AB':6, 'AC':0,
  'BA':0, 'BB':3, 'BC':6,
  'CA':6, 'CB':0, 'CC':3,
}

choice_points = {
  'A':1, 'B':2, 'C':3,
  'X':1, 'Y':2, 'Z':3,
}

choice_points2 = {
  'A':1, 'B':2, 'C':3,
  'X':0, 'Y':3, 'Z':6,
}

loser = {
  'A':'C',
  'B':'A',
  'C':'B',
}

winner = {
  'A':'B',
  'B':'C',
  'C':'A',
}

outcome_points = {
  'AX':3, 'AY':6, 'AZ':0,
  'BX':0, 'BY':3, 'BZ':6,
  'CX':6, 'CY':0, 'CZ':3,
}

def handle_turn(turn: str) -> str:
  op_choice = turn[0]
  my_choice = turn[1]
  new_choice = ''
  if my_choice == 'X':
    new_choice = loser[op_choice]
  elif my_choice == 'Y':
    new_choice = op_choice
  elif my_choice == 'Z':
    new_choice = winner[op_choice]
  else:
    print('invalid choice:', my_choice)

  return op_choice + new_choice

# first part of day 2
def solve(inputdata):
  score = 0 
  for i, line in enumerate(inputdata):
    if line == '': break
    line = line.replace(' ', '')
    this_score = outcomes[line] + choices[line[1]]
    score += this_score
    print(i, '>', line, ':', this_score)
  print(score)

# seocnd part of day 2 (slightly adjusted)
def solve2(inputdata):
  score = 0
  for i, line in enumerate(inputdata):
    if line == '': break
    line = line.replace(' ', '')
    line = handle_turn(line)
    this_score = turn_points[line] + choice_points2[line[1]]
    print(i, '>', line, ':', turn_points[line], choice_points2[line[1]], this_score)
    #print(i, '>', line, ':', this_score)
    score += this_score
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


#print(testinput)
#solve2(testinput)
solve2(realinput)


