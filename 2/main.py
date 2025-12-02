import textwrap

def get_invalid_ids(ids):

    invalid_sum = 0

    for id in ids:
        str_id = str(id)
        id_length = len(str_id)
        if id_length % 2 != 0:
            continue

        p1 = str_id[:int(id_length/2)]
        p2 = str_id[int(id_length/2):]

        if p1 == p2:
            invalid_sum += id

    return invalid_sum

def get_invalid_ids_p2(ids):

    invalid_sum = 0

    for id in ids:
        str_id = str(id)
        id_length = len(str_id)

        for it in range(1, id_length+1):

            if id_length % it == 0 and it != 1:
                divisor = it

                parts = textwrap.wrap(str_id, int(id_length/divisor))

                if len(set(parts)) == 1:
                    invalid_sum += id
                    break

    return invalid_sum

def extract_ids(ranges):

    ids = []

    for str_range in ranges:
        split_range = str_range.split("-")

        start = int(split_range[0])
        end = int(split_range[1])
        span = end-start


        for i in range(span+1):
            id = start + i
            ids.append(id)

    return ids


with open("2/input.txt", "r") as input_file:
    ranges_string = input_file.readline().rstrip()

ranges = ranges_string.split(",")
all_ids = extract_ids(ranges)

print(
    get_invalid_ids(all_ids)
)

print(
    get_invalid_ids_p2(all_ids)
)


