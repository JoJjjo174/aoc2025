

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
