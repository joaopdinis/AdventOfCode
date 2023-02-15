from regex import findall
from collections import defaultdict

radar = defaultdict(str)

y = 2000000
count = 0

    
for i in range(2):
    for l in open('input.txt'):
        if l == '\n':
            continue

        coords = [int(s) for s in findall('-?\d+', l.strip())]

        if i == 0:
            radar[tuple(coords[:2])] = 'S'
            radar[tuple(coords[2:])] = 'B'
        else:
            sensor = coords[:2]
            beacon = coords[2:]
            x = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
            k = x - abs(sensor[1] - y)
            for i in range(sensor[0] - k, sensor[0] + k + 1):
                if radar[(i,y)] == '':
                    radar[(i,y)] = '#'
                    count = count + 1

print(count)