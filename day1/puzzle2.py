input = [l.strip() for l in open('input.txt')]


food_list = []

total_calories = 0

for food in input:
    if food != '':
        total_calories += int(food)
    else:
        food_list.append(total_calories)
        total_calories = 0

print(sum(sorted(food_list, reverse=True)[:3]))
