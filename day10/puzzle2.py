instructions = [l.strip().split(' ') for l in open('input.txt')]

cycle = 1
index = 0
X = 1
is_computing = False

signal_strength = 0

while index < len(instructions):
    print('🎅', end='') if X - 1 <= (cycle-1)%40 <= X + 1 else print('🎄', end='')
    if cycle % 40 == 0:
        print()
    if is_computing:
        X += int(instructions[index][1])
        is_computing = False
        index += 1
    else:
        if instructions[index][0] == 'addx':
            is_computing = True
        else:
            index += 1
    cycle += 1