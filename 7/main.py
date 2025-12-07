
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

def recursive_drop(grid, row_i, col_i, percentage_index): # too slow

    while grid[row_i][col_i] != "^":
        if row_i == len(grid)-1:
            return 1

        row_i += 1

    if row_i == percentage_index:
        print(".")

    res = recursive_drop(grid, row_i, col_i+1, percentage_index)
    if row_i == percentage_index:
        print("Done")

    res2 = recursive_drop(grid, row_i, col_i-1, percentage_index)
    if row_i == percentage_index:
        print("Done")

    return res + res2

def merge_beams(beams):

    column_values = {}
    for beam in beams:
        if beam.column in column_values:
            column_values[beam.column] += beam.value

        else:
            column_values[beam.column] = beam.value

    new_beams = [Beam(column_value, column_values[column_value]) for column_value in column_values]

    return new_beams



def p2(grid):
    beams = [
        Beam(find_starting_column(grid[0]))
    ]
    row_index = 1

    while row_index < len(grid):
        row = grid[row_index]

        new_beams = []
        for beam_obj in beams:
            if row[beam_obj.column] == "^":
                new_beams.append(Beam(beam_obj.column-1, beam_obj.value))
                new_beams.append(Beam(beam_obj.column+1, beam_obj.value))

            else:
                new_beams.append(Beam(beam_obj.column, beam_obj.value))

        beams = merge_beams(new_beams)
        row_index += 1

    total_value = 0
    for beam in beams:
        total_value += beam.value

    return total_value

class Beam():
    def __init__(self, column, value=1):
        self.column = column
        self.value = value

grid = []

with open("7/input.txt", "r") as file:
    for line in file.readlines():
        grid.append(line.rstrip())

print(
    p1(grid)
)

#print(
#    recursive_drop(grid, 0, find_starting_column(grid[0]), 20)
#)

print(
    p2(grid)
)
