instructions = [l.strip().split(' ') for l in open('input.txt')]

cycle = 1
index = 0
X = 1
is_computing = False

check_cycle = [20, 60, 100, 140, 180, 220]

signal_strength = 0

while index < len(instructions):
    if cycle in check_cycle:
        signal_strength += cycle * X
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
        
print(signal_strength)