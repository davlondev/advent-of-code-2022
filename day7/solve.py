

def get_input(file_path):
  with open(file_path) as f:
    lines = f.readlines()
  f.close()
  for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')
  return lines

def get_command(line):
  x = line.split(' ')[1]
  return x

def get_size(line):
  s = line.split(' ')[0]
  return s

def solve(data):

  total = 0
  limit = 100000
  cur_sum = 0
  cur_folder = ""

  logs = ""

  # keep track of folders
  folders = {}

  for line in data:
    
    if cur_folder != "" and cur_folder[len(cur_folder)-1] != '/':
      cur_folder += '/'
    if cur_folder == '': cur_folder = '/'
    if cur_folder not in folders:
      folders[cur_folder] = 0

    if line[0] != '$':

      size = get_size(line)

      if size == 'dir': continue
      else: size = int(size)

      file_name = line.split(' ')[1]
      cur_sum += size
      folders[cur_folder] += size
      print('--- ' * cur_folder.count('/') + file_name, size)

    elif line[0] == '$':
      cmd = get_command(line)

      if cmd == 'cd':
        print('total size', cur_sum)

        if cur_sum <= limit:
          logs += f"[Log] Added {cur_sum} to {total} = {total+cur_sum}\n"
          total += cur_sum
        cur_sum = 0

        target_folder = line.split(' ')[2]

        if target_folder == '..':
          cur_folder = '/' + ''.join(cur_folder.split('/')[:-2])
        elif target_folder == '/':
          cur_folder = '/'
        else:
          cur_folder += target_folder + '/'

        print(f'\nfolder: "{cur_folder}"')


  print()
  print(total)
  print()
  print(logs)
  print(folders)

data = get_input('testinput.txt')
#data = get_input('input.txt')

solve(data)
