import turtle

def print_grid(rope):
    rows = 21
    cols = 26
    origin = [5,11]
    for i in range(rows-1, -1, -1):
        for j in range(cols):
            if [i,j] in rope:
                if rope.index([i,j]) != 0:
                    print(rope.index([i,j]), end='') 
                else:
                    print('H', end='')
            else:
                if [i,j] == origin:
                    print('s', end='')
                else:
                    print('.', end='')
                
        print()
    print()




input = [l.strip() for l in open('input.txt')]


origin = (0,0)
positions_visited = {origin}

rope_length = 10

rope = [[origin[0], origin[1]] for i in range(rope_length)]

wn = turtle.Screen()

turtle.Screen().bgcolor("black")

def draw_tale(tale):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.goto(tale[1]*20, tale[0]*20)
    t.shape("square")
    t.color("yellow")
    t.showturtle()

def update_turtle(index, knot):
    if index == rope_length-1:
        draw_tale(knot)
        
    rope_turtle[index].goto(knot[1]*20, knot[0]*20)
    wn.update()

rope_turtle = []

for i in range(rope_length):
    knot = turtle.Turtle()
    knot.speed(0)
    knot.penup()
    knot.hideturtle()
    knot.goto(origin[0]*20, origin[1]*20)
    knot.shape("square")
    if i == 0:          
        knot.color("red")
    else:
        knot.color('white')
    knot.showturtle()

    rope_turtle.append(knot)

draw_tale(rope[rope_length-1])

wn.update()

def draw_tale(tale):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    t.goto(tale[1]*20, tale[0]*20)
    t.shape("square")
    t.color("yellow")
    t.showturtle()

def update_turtle(index, knot):
    if index == rope_length-1:
        draw_tale(knot)
        
    rope_turtle[index].goto(knot[1]*20, knot[0]*20)
    wn.update()




for line in input:
    line = line.split()
    direction = line[0]
    steps = int(line[1])

    dir = {'U': [0,1,1], 'D': [0,-1,1], 'R': [1,1,0], 'L': [1,-1,0]}

    # print("\n== {} {} ==\n".format(direction, steps))

    for i in range(steps):
        rope[0][dir[direction][0]] += dir[direction][1]
        # print("== step {} ==".format(i+1))
        # print("== Moving H ==")
        # print_grid(rope)
        update_turtle(0, rope[0])
        curr_dir = direction
        for j, knot in enumerate(rope[1:], 1):
            if abs(rope[j-1][0] - rope[j][0]) > 1 or abs(rope[j-1][1] - rope[j][1]) > 1:
                # print("== Moving {} ==".format(j))

                if rope[j-1][1] == rope[j][1]:
                    if rope[j-1][0] > rope[j][0]: 
                        rope[j][0] += 1
                        curr_dir = 'U' 
                    else: 
                        rope[j][0] -= 1
                        curr_dir = 'D' 

                elif rope[j-1][0] == rope[j][0]:
                    if rope[j-1][1] > rope[j][1]: 
                        rope[j][1] += 1  
                        curr_dir = 'R' 
                    else: 
                        rope[j][1] -= 1
                        curr_dir = 'L' 
                
                else:
                    rope[j][dir[curr_dir][0]] += dir[curr_dir][1]

                    if rope[j-1][dir[curr_dir][2]] > rope[j][dir[curr_dir][2]]:
                        rope[j][dir[curr_dir][2]] += 1
                    elif rope[j-1][dir[curr_dir][2]] < rope[j][dir[curr_dir][2]]:
                        rope[j][dir[curr_dir][2]] -= 1

                if j == rope_length - 1: positions_visited.add((rope[j][0], rope[j][1]))
                # print_grid(rope)
                update_turtle(j, rope[j])          

print(rope)
print(len(positions_visited))


turtle.mainloop()