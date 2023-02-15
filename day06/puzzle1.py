input = [l.strip() for l in open('input.txt')][0]

for i in range(len(input)):
    if len(set(input[i:i+4])) == 4:
        print(i+4)
        break
