from functools import cmp_to_key

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

input = [eval(l.strip()) for l in open('input.txt') if l != '\n'] + [[[2]],[[6]]]

input.sort(key=cmp_to_key(pair_in_right_order))
print((input.index([[2]])+1) * (input.index([[6]])+1))