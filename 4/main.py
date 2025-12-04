
def get_accessable_paper(diagram):

    accessable_locations = []
    accessable = 0

    for row_i, row in enumerate(diagram):
        for column_i, _ in enumerate(row):
            
            adjecant = 0

            for delta_x in [-1, 0, 1]:
                for delta_y in [-1, 0, 1]:
                    if delta_x == 0 and delta_y == 0:
                        continue

                    x = row_i + delta_x
                    y = column_i + delta_y

                    if x > len(diagram)-1 or x < 0 or y > len(row)-1 or y < 0:
                        continue

                    if diagram[x][y] == "@":
                        adjecant += 1

            if adjecant < 4 and row[column_i] == "@":
                accessable_locations.append((row_i, column_i))    
                accessable += 1

    return accessable, accessable_locations

def get_accessable_paper_p2(diagram):
    
    total_accessable = 0
    current_diagram = diagram

    while True:
        amount, locations = get_accessable_paper(current_diagram)

        if amount == 0:
            break
        total_accessable += amount

        current_diagram = remove_locations(current_diagram, locations)

    return total_accessable

def remove_locations(diagram, locations):
    new_diagram = []

    for row_i, row in enumerate(diagram):
        new_row = row
        for col_i, col in enumerate(row):


            loc = (row_i, col_i)
            if loc in locations:
                new_row = new_row[:col_i] + "." + new_row[col_i+1:]

        new_diagram.append(new_row)

    return new_diagram

with open("4/input.txt", "r") as file:
    inp = []
    for line in file.readlines():
        inp.append(line.rstrip())

print(
    get_accessable_paper(inp)[0]
)

print(
    get_accessable_paper_p2(inp)
)
