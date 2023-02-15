input = [l.strip() for l in open('input.txt')]

max_calories = 0
total_calories = 0

for food in input:
    if food != '':
        total_calories += int(food)
    else:
        max_calories = max(total_calories, max_calories)
        total_calories = 0

print(max_calories)
