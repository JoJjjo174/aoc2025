
class Region():
    def __init__(self, width, height, required_shapes):
        self.width = width
        self.height = height
        self.required_shapes = required_shapes

    def can_contain(self):
        area = self.width * self.height

        required_area = 0
        for shape_i, amount in enumerate(self.required_shapes):
            shape = shapes[shape_i]

            for row in shape:
                required_area += sum(row) * amount

        return area >= required_area

def p1():
    total = 0
    for r in regions:
        total += 1 if r.can_contain() else 0

    return total

shapes = []
regions = []
with open("12/input.txt", "r") as file:
    in_shape = False
    shape = []
    for line in file.readlines():
        stripped_line = line.rstrip()

        if len(stripped_line) == 2:
            in_shape = True
            continue

        if in_shape:
            if stripped_line == "":
                in_shape = False
                shapes.append(shape.copy())
                shape = []
                continue

            shape.append(
                [i == "#" for i in stripped_line]
            )
            continue

        split_line = stripped_line.split()
        width, height = [ int(i) for i in split_line[0][:-1].split("x")]
        required_shapes = [ int(i) for i in split_line[1:]]

        regions.append(
            Region(width, height, required_shapes.copy())
        )

# ! Likely doesn't work on more complicated inputs, as it only compares the areas, and doesn't actually try to find the best fit
print(
    p1()
)
