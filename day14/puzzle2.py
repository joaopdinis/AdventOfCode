from collections import defaultdict

input = [[tuple(map(int, coordinate.split(","))) for coordinate in line.split("->")] for line in open('input.txt') if line != '\n']

scan = defaultdict(str)

def draw_rocks(coord1, coord2):
    for i in range(min(coord1[0],coord2[0]), max(coord1[0],coord2[0])+1):
        for j in range(min(coord1[1],coord2[1]), max(coord1[1],coord2[1])+1):
            scan[(i, j)] = '#'


height = 0
for coordinates in input:
    for coord1, coord2 in zip(coordinates,coordinates[1:]):
        draw_rocks(coord1, coord2)
        height = max(height, coord1[1], coord2[1])

sand = [500, 0]


floor  = height + 2
sands = 0
while True:
    if sand[1]+1 == floor:
        scan[(sand[0], sand[1])] = 'o'
        sands += 1
        sand = [500, 0]
    if scan[(sand[0], sand[1]+1)] == '':
        sand = [sand[0], sand[1]+1]
    elif scan[(sand[0]-1, sand[1]+1)] == '':
        sand = [sand[0]-1, sand[1]+1]
    elif scan[(sand[0]+1, sand[1]+1)] == '':
        sand = [sand[0]+1, sand[1]+1]
    elif sand[1] == 0:
        scan[(sand[0], sand[1])] = 'o'
        sands += 1
        break
    else:
        scan[(sand[0], sand[1])] = 'o'
        sands += 1
        sand = [500, 0]
        
print(sands)
