from collections import defaultdict

def get_new_path(path):
	i = len(path)
	for i in range(len(path)-2, -1, -1):
		if path[i] == '/':
			break
	return path[:i+1]

input = [l.strip() for l in open('input.txt')]


dir_dict = defaultdict(int)
dir_seen = []
dir_size = 0

solution = 70000000
path = ''

for line in input:
	cmd = line.split()

	if cmd[0] == '$' and cmd[1] == 'cd':
		if cmd[2] == '..':
			dir_dict[dir_seen[-1]] += dir_size
			dir_size = 0
			child_total_size = dir_dict[dir_seen[-1]]

			dir_seen.pop(-1)
			
			path = get_new_path(path)

			dir_dict[dir_seen[-1]] += child_total_size
		elif cmd[2] == '/':
			path = '/'
			dir_seen.append(path)
			dir_size = 0
		else:
			dir_dict[dir_seen[-1]] += dir_size
			dir_size = 0
			path += cmd[2] + '/'
			dir_seen.append(path)

	elif cmd[0] != '$' and cmd [0] != 'dir':
		dir_size += int(cmd[0])
    
while len(dir_seen) >= 2:
	dir_dict[dir_seen[-1]] += dir_size
	dir_size = 0
	child_total_size = dir_dict[dir_seen[-1]]

	dir_seen.pop(-1)

	dir_dict[dir_seen[-1]] += child_total_size


total_size = dir_dict['/']
for key, value in dir_dict.items():
	if value <= solution and total_size - value < 40000000:
		solution = value

print(solution)