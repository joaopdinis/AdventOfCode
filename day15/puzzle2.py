from regex import findall

squares = []

low, top = 0, 4_000_000


def find_next_right(pos):
    limit = None
    for square in squares:
        x = abs(square[0]-square[2]) + abs(square[1]-square[3])
        k = x - abs(square[1] - pos[1])

        if k >= 0 and square[0] - k <= pos[0] <= square[0] + k:
            
            if limit == None:
                limit = square[0] + k
            else:
                limit = max(square[0] + k, limit) 
    
    return limit

for l in open('input.txt'):
    if l == '\n':
        continue

    coords = [int(s) for s in findall('-?\d+', l.strip())]
    squares.append(coords)

curr_pos = (0,0)

while True:
    limit_right = find_next_right(curr_pos)
    if limit_right != None:
        if limit_right < top:
            curr_pos = (limit_right+1, curr_pos[1])
        else:
            curr_pos = (0, curr_pos[1]+1)
    else:
        break

print(4000000*curr_pos[0] + curr_pos[1])
