
def get_accessable_paper(diagram):

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
                accessable += 1


    return accessable


with open("4/input.txt", "r") as file:
    inp = []
    for line in file.readlines():
        inp.append(line.rstrip())

print(
    get_accessable_paper(inp)
)
