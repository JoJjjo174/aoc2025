from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt

def p1(red_tiles):

    biggest = 0

    for i, i_location in enumerate(red_tiles):
        for j, j_location in enumerate(red_tiles):
            if j <= i:
                continue

            x_diff = abs(i_location[0] - j_location[0]) + 1
            y_diff = abs(i_location[1] - j_location[1]) + 1

            area = x_diff * y_diff

            if area > biggest:
                biggest = area

    return biggest

def p2(red_tiles):


    shape = Polygon(red_tiles)

    biggest = 0
    biggest_shape = None
    for i, i_location in enumerate(red_tiles):
        for j, j_location in enumerate(red_tiles):
            if j <= i:
                continue

            #x_diff = abs(i_location[0] - j_location[0] + 1)
            #y_diff = abs(i_location[1] - j_location[1] + 1)

            area = (abs(i_location[0] - j_location[0]) + 1) * (abs(i_location[1] - j_location[1]) + 1)

            if area > biggest:

                corners = [
                    (min((i_location[0], j_location[0])), min((i_location[1], j_location[1]))),
                    (min((i_location[0], j_location[0])), max((i_location[1], j_location[1]))),
                    (max((i_location[0], j_location[0])), max((i_location[1], j_location[1]))),
                    (max((i_location[0], j_location[0])), min((i_location[1], j_location[1])))
                ]
                area_shape = Polygon(corners)

                if not shape.contains(area_shape):
                    continue

                biggest_shape = area_shape
                biggest = area

    print(biggest_shape)

    fig, axs = plt.subplots()
    axs.set_aspect("equal", "datalim")

    xs, ys = shape.exterior.xy    
    axs.fill(xs, ys, alpha=0.5, fc="r", ec="none")

    xs, ys = biggest_shape.exterior.xy    
    axs.fill(xs, ys, alpha=0.5, fc="r", ec="none")

    for tile in red_tiles:
        plt.plot(tile[0],tile[1],"ro") 

    plt.show()

    return biggest   

direct_connections = []
red_tiles = []
with open("9/input.txt", "r") as file:
    prev_tile = ()

    f = True
    for line in file.readlines():
        x, y = line.rstrip().split(",")
        tile = (int(x), int(y))

        if f:
            prev_tile = tile 
            f = False

        else:
            direct_connections.append(
                ((prev_tile), tile)
            )
            prev_tile = tile 

        red_tiles.append(tile)

    direct_connections.append(
        (red_tiles[len(red_tiles)-1], red_tiles[0])
    )

print(
    p1(red_tiles)
)

print(
    p2(red_tiles)
)
# 1 540 157 850 too low
# 
# 1 540 192 500
#
# 1 636 630 590 too high
