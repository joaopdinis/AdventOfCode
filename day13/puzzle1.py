
def pair_in_right_order(left, right):
    for i in range(max(len(left), len(right))):
        if i >= len(left) or i >= len(right):
            return len(left) - len(right)

        if type(left[i]) is list or type(right[i]) is list:
            l = [left[i]] if type(left[i]) is not list else left[i]
            r = [right[i]] if type(right[i]) is not list else right[i]
            x = pair_in_right_order(l, r)

            if x: return x
        
        else:
            if left[i] != right[i]: return left[i] - right[i]

    return 0

input = [eval(l.strip()) for l in open('input.txt') if l != '\n']
pair = 1
solution = 0
for i in range(0, len(input), 2):
    print(f'{pair} - Right Order') if pair_in_right_order(input[i], input[i+1]) <= 0 else print(f'{pair} - Wrong Order')
    if pair_in_right_order(input[i], input[i+1]): solution += pair
    pair += 1

print(solution)
