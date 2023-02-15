def BFS(map, src, dest, dist):

    visited = [[False] * len(map[i]) for i in range(len(map))]

    queue = [src]

    visited[src[0]][src[1]] = True
    dist[src[0]][src[1]] = 0

    while queue:
        v = queue.pop(0)

        for next_pos in get_possible_path(map, v[0], v[1]):
            if not visited[next_pos[0]][next_pos[1]]:
                queue.append(next_pos)
                visited[next_pos[0]][next_pos[1]] = True
                dist[next_pos[0]][next_pos[1]] = dist[v[0]][v[1]] + 1

                if next_pos == dest:
                    return
    
def get_shortest_distance(map, src, dest):
    dist = [[1000000] * len(map[i]) for i in range(len(map))]

    BFS(map, src, dest, dist)

    return dist[dest[0]][dest[1]]


def get_possible_path(map, posX, posY):
    possible_path = []
    curr_pos_height = map[posX][posY]

    # left is possible
    if posY > 0 and ord(map[posX][posY-1]) - ord(curr_pos_height) <= 1:
        possible_path.append((posX, posY-1))
    # right is possible
    if posY < len(map[posX])-1 and ord(map[posX][posY+1]) - ord(curr_pos_height) <= 1:
        possible_path.append((posX, posY+1))
    # up is possible
    if posX > 0 and ord(map[posX-1][posY]) - ord(curr_pos_height) <= 1:
        possible_path.append((posX-1, posY))
    # down is possible
    if posX < len(map)-1 and ord(map[posX+1][posY]) - ord(curr_pos_height) <= 1:
        possible_path.append((posX+1, posY))

    return possible_path

map = []
src= ()
dest= ()
for i, l in enumerate(open('input.txt')):
    row = []
    for j, x in enumerate(l.strip()):
        if x == 'S':
            src = (i,j)
            x = 'a'
        elif x == 'E':
            dest = (i,j)
            x = 'z'
        row.append(x)
    map.append(row)


print(get_shortest_distance(map, src, dest))
