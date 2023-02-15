INF = 2 ** 64

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
    
def get_shortest_distance(map, square_a, dest):
    min_dist = INF
    for square in square_a:
        dist = [[INF] * len(map[i]) for i in range(len(map))]
        BFS(map, square, dest, dist)
        min_dist = min(min_dist, dist[dest[0]][dest[1]])

    return min_dist


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
square_a = []
for i, l in enumerate(open('input.txt')):
    row = []
    for j, x in enumerate(l.strip()):
        if x == 'S':
            src = (i,j)
            x = 'a'
        elif x == 'E':
            dest = (i,j)
            x = 'z'
        
        if x == 'a':
            square_a.append((i,j))

        row.append(x)
    map.append(row)

print(get_shortest_distance(map, square_a, dest))
