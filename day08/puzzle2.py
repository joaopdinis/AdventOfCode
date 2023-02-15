def count_trees(grid, pos, curr_height, dir):
    if dir == 'bottom':
        low = pos[0]+1
        top = len(grid)
        for_dir = 1
    elif dir == 'up':
        low = pos[0]-1
        top = -1
        for_dir = -1
    elif dir == 'left':
        low = pos[1]-1
        top = -1
        for_dir = -1
    elif dir == 'right':
        low = pos[1]+1
        top = len(grid[pos[0]])
        for_dir = 1

    count = 0
    for i in range(low, top, for_dir):
        count += 1
        tree_height = int(grid[i][pos[1]]) if dir == 'bottom' or dir == 'up' else int(grid[pos[0]][i])
        if tree_height >= curr_height:
            break
    
    return count



grid = [l.strip() for l in open('input.txt')]

best_scenic_score = 0

for i in range(1, len(grid)-1):
    for j in range(1, len(grid)-1):
        tree_height = int(grid[i][j])
        trees_visible_bottom = count_trees(grid, (i,j), tree_height, 'bottom')
        trees_visible_up = count_trees(grid, (i,j), tree_height, 'up')
        trees_visible_left = count_trees(grid, (i,j), tree_height, 'left')
        trees_visible_right = count_trees(grid, (i,j), tree_height, 'right')

        best_scenic_score = max(best_scenic_score, trees_visible_bottom * trees_visible_up * trees_visible_left * trees_visible_right)
 
print(best_scenic_score)