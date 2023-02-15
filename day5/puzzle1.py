from collections import defaultdict

def get_stacks(stack_text):
    stacks = defaultdict(list)

    for row in reversed(stack_text.split('\n')[:-3]):
        for stack, crate in enumerate(row[1::4], start=1):
            if crate != ' ':
                stacks[stack].append(crate)
    return stacks


input = [l for l in open('input.txt')]

stack_text = ''

read_stack = True
for l in input:
    if read_stack:
        stack_text += l
    else:
        numbers = [int(x) for x in l.split() if x.isnumeric()]
        move_quantity = numbers[0]
        move_from = numbers[1]
        move_to = numbers[2]
        [stacks[move_to].append(stacks[move_from].pop(-1)) for i in range(move_quantity)]
    if l == '\n':
        read_stack = False
        stacks = get_stacks(stack_text)
        print(stacks)


solution = [crate[-1] for crate in stacks.values()]

print(''.join(solution))
