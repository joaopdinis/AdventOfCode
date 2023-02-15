def get_points(round):
    opoonent_choice = round[0]
    my_choice = round[1]

    index = {'A': 0, 'X': 0, 'B': 1, 'Y': 1, 'C': 2, 'Z': 2}

    points_board = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

    return points_board[index[opoonent_choice]][index[my_choice]]




input = [l.strip() for l in open('input.txt')]

score = 0

for round in input:
    score += get_points(round.split(' '))


print(score)