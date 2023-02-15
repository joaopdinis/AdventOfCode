input = [l.strip() for l in open('input.txt')][0]

for i in range(len(input)):
    if len(set(input[i:i+14])) == 14:
        print(i+14)
        break
