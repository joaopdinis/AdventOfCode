def is_assignment_overlaped(pair1, pair2):

    pair1_low = int(pair1[0])
    pair1_top = int(pair1[1])
    pair2_low = int(pair2[0])
    pair2_top = int(pair2[1])

    if pair1_low >= pair2_low and pair1_top <= pair2_top:
        return True
    elif pair2_low >= pair1_low and pair2_top <= pair1_top:
        return True
    else:
        return False
        

input = [l.strip() for l in open('input.txt')]

total_overlaps = 0

for assign_pairs in input:
    pairs = assign_pairs.split(',')
    pair1 = pairs[0].split('-')
    pair2 = pairs[1].split('-')

    overlap = is_assignment_overlaped(pair1, pair2)
    total_overlaps += overlap

print(total_overlaps)