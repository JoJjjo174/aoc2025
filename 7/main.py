
def find_starting_column(starting_row):
    return starting_row.find("S")

def visualize(row, beams):
    row_list = list(row)

    for beam in beams:
        row_list[beam] = "|"
    
    return "".join(row_list)

def p1(grid):
    splits = 0
    beams = [
        find_starting_column(grid[0])
    ]
    row_index = 1

    print(visualize(grid[0], beams))

    while row_index < len(grid):
        row = grid[row_index]

        new_beams = []
        for beam_index in beams:
            if row[beam_index] == "^":
                splits += 1

                new_beams.append(beam_index-1)
                new_beams.append(beam_index+1)

            else:
                new_beams.append(beam_index)

        print(visualize(grid[row_index], new_beams))

        beams = list(set(new_beams))
        row_index += 1

    return splits

grid = []

with open("7/input.txt", "r") as file:
    for line in file.readlines():
        grid.append(line.rstrip())

print(
    p1(grid)
)
