input = [l.strip() for l in open('input.txt')]

origin = (0,0)
positions_visited = {origin}

rope_length = 10

rope = [[origin[0], origin[1]] for i in range(rope_length)]

for line in input:
    line = line.split()
    direction = line[0]
    steps = int(line[1])

    dir = {'U': [0,1,1], 'D': [0,-1,1], 'R': [1,1,0], 'L': [1,-1,0]}

    for i in range(steps):
        rope[0][dir[direction][0]] += dir[direction][1]
        curr_dir = direction

        for j, knot in enumerate(rope[1:], 1):
            if abs(rope[j-1][0] - rope[j][0]) > 1 or abs(rope[j-1][1] - rope[j][1]) > 1:
                if rope[j-1][1] == rope[j][1]:
                    if rope[j-1][0] > rope[j][0]: 
                        rope[j][0] += 1
                        curr_dir = 'U' 
                    else: 
                        rope[j][0] -= 1
                        curr_dir = 'D' 
                elif rope[j-1][0] == rope[j][0]:
                    if rope[j-1][1] > rope[j][1]: 
                        rope[j][1] += 1  
                        curr_dir = 'R' 
                    else: 
                        rope[j][1] -= 1
                        curr_dir = 'L'                 
                else:
                    rope[j][dir[curr_dir][0]] += dir[curr_dir][1]

                    if rope[j-1][dir[curr_dir][2]] > rope[j][dir[curr_dir][2]]:
                        rope[j][dir[curr_dir][2]] += 1
                    elif rope[j-1][dir[curr_dir][2]] < rope[j][dir[curr_dir][2]]:
                        rope[j][dir[curr_dir][2]] -= 1

                if j == rope_length - 1: positions_visited.add((rope[j][0], rope[j][1]))

print(len(positions_visited))