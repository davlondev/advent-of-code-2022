

def prep_input(filename):
  with open(filename) as f:
    lines = f.readlines()
  f.close()
  return lines

data = prep_input("input.txt")

def is_unique(s: str) -> bool:
  l = len(s)
  for i in range(l):
    cur_letter_1 = s[i]
    for k in range(l):
      if k == i: continue
      cur_letter_2 = s[k]
      if cur_letter_1 == cur_letter_2:
        return False
  return True

def solve(s: str):

  line = s
  print('line:', line)
  print('length:', len(line))
  print('\n')
  packet_size = 14 # 4 for part 1, 14 for part 2

  letters = ''

  i = 0 
  while i <= len(line)-packet_size:
    letters = line[i:i+packet_size]
    u = is_unique(letters)
    if u: 
      print('unique found:', letters)
      break
    i+= 1

  print('unique index:', i+packet_size)
  return i+packet_size

#solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
#solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
data = prep_input('input.txt')[0]
solve(data)
