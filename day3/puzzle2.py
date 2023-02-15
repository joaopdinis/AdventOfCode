def find_priority(rucksacks):
    item_in_rucksacks = list(rucksacks[0].strip())
    
    for i in range(1, len(rucksacks)):
        rucksack = rucksacks[i]
        shared_items = []
        for item in rucksack:
            if item in item_in_rucksacks:
                shared_items.append(item)
        
        item_in_rucksacks = shared_items

    shared_item = shared_items[0]

    if ord(shared_item) < ord('a'): # It's uppercase
        return ord(shared_item) - ord('A') + 27
    else:
        return ord(shared_item) - ord('a') + 1


input = [l.strip() for l in open('input.txt')]

priorities_sum = 0 
for rucksack1, rucksack2, rucksack3 in zip(*[iter(input)]*3):
    priority = find_priority([rucksack1, rucksack2, rucksack3])
    priorities_sum += priority

print(priorities_sum)
