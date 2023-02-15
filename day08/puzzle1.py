grid = [l.strip() for l in open('input.txt')]

row = len(grid) * [-1]
col = len(grid[0]) * [-1]

trees_visible = 0

for i in range(len(grid)):
    for j in range(len(grid)):
        tree_height = int(grid[i][j])
        if tree_height > row[i] or tree_height > col[j]:
            row[i] = max(row[i], tree_height)    
            col[j] = max(col[j], tree_height)
            trees_visible += 1
        elif i == len(grid) - 1 or j == len(grid[i]) - 1:
            trees_visible += 1
        else:
            max_bottom = max([int(grid[k][j]) for k in range(i+1, len(grid))])
            max_right = max([int(grid[i][k]) for k in range(j+1, len(grid[i]))])
            if tree_height > max_bottom or tree_height > max_right:
                trees_visible += 1
        
print(trees_visible)