
def p1(red_tiles):

    biggest = 0

    for i, i_location in enumerate(red_tiles):
        for j, j_location in enumerate(red_tiles):
            if j <= i:
                continue

            x_diff = abs(i_location[0] - j_location[0] + 1)
            y_diff = abs(i_location[1] - j_location[1] + 1)

            area = x_diff * y_diff

            if area > biggest:
                biggest = area

    return biggest

red_tiles = []
with open("9/input.txt", "r") as file:
    for line in file.readlines():
        x, y = line.rstrip().split(",")
        
        red_tiles.append((int(x), int(y)))

print(
    p1(red_tiles)
)

