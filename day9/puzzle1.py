input = [l.strip() for l in open('input.txt')]

positions_visited = {(0,0)}

tail = [0,0]
head = [0,0]

for line in input:
    line = line.split()
    direction = line[0]
    steps = int(line[1])

    dir = {'U': [0,1,1], 'D': [0,-1,1], 'R': [1,1,0], 'L': [1,-1,0]}

    for i in range(steps):
        print([head, tail])
        head[dir[direction][0]] += dir[direction][1]
        if abs(head[dir[direction][0]] - tail[dir[direction][0]]) > 1:
            tail[dir[direction][0]] += dir[direction][1]
            tail[dir[direction][2]] = head[dir[direction][2]]
            positions_visited.add((tail[0], tail[1]))
    
print(len(positions_visited))