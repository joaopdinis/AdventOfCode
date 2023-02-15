def find_priority(rucksack):
    shared_item = ''
    item_in_first_half = []
    
    for i in range(len(rucksack)):
        item = rucksack[i]

        if i < len(rucksack)/2:
            item_in_first_half.append(item)
        else:
            if item in item_in_first_half:
                shared_item = item
                break

    if ord(shared_item) < ord('a'): # It's uppercase
        return ord(shared_item) - ord('A') + 27
    else:
        return ord(shared_item) - ord('a') + 1


input = [l.strip() for l in open('input.txt')]

priorities_sum = 0 
for rucksack in input:
    priority = find_priority(rucksack)
    priorities_sum += priority

print(priorities_sum)