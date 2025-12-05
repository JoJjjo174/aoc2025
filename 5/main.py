

def get_ids_in_range(ranges, ids):

    in_range = 0

    for id in ids:
        for range in ranges:
            split_range = range.split("-")
            start = int(split_range[0])
            end = int(split_range[1])

            if start <= id and end >= id:
                in_range += 1
                break

    return in_range

def p2(ranges):

    int_ranges = []
    for range_ in ranges:
        split_range = range_.split("-")
        start = int(split_range[0])
        end = int(split_range[1])

        int_ranges.append((start, end))

    old_length = float("inf")

    while len(int_ranges) != old_length:
        old_length = len(int_ranges)
        int_ranges = list_combine(int_ranges.copy())
    
    total = 0

    for i in int_ranges:
        total += i[1] - i[0] + 1

    return total
    

def list_combine(int_ranges):
    new_ranges = []

    while len(int_ranges) > 0:
        range_ = int_ranges[0]

        int_ranges.pop(0)
        ranges_copy = int_ranges.copy()
        while len(ranges_copy) > 0:
            other_range = ranges_copy[0]

            if is_overlapping(range_, other_range):
                int_ranges.remove(other_range)
                range_ = combine(range_, other_range)
            
            ranges_copy.pop(0)

        new_ranges.append(range_)

    return new_ranges

def is_overlapping(range1, range2):
    if range1[0] < range2[0]:
        ranges = (range1, range2)

    else:
        ranges = (range2, range1)

    _, end_1 = ranges[0]
    start_2, _ = ranges[1]

    return end_1 >= start_2

def combine(range1, range2):
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))

with open("5/input.txt", "r") as file:
    ids = []
    ranges = []
    seperator = False

    for line in file.readlines():
        stripped = line.rstrip()
        
        if stripped == "":
            seperator = True
            continue

        if not seperator:
            ranges.append(stripped)

        else:
            ids.append(int(stripped))

print(
    get_ids_in_range(ranges, ids)
)

print(
    is_overlapping((3,5), (1,100))
)

print( # Too high
    p2(ranges)
)
