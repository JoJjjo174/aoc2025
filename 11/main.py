
class Node():
    def __init__(self, name, outwards_connections):
        self.name = name
        self.outwards_connections = outwards_connections

    def discover(self):
        if self.name == "out":
            return 1
        
        total = 0
        for connection in self.outwards_connections:
            other_node = nodes[connection]
            total += other_node.discover()

        return total
    
nodes = {}
with open("11/input.txt", "r") as file:
    for line in file.readlines():
        split_line = line.rstrip().split()

        name = split_line[0][:-1]
        outwards_connections = split_line[1:]

        nodes[name] = Node(name, outwards_connections)

nodes["out"] = Node("out", [])

print(
    nodes["you"].discover()
)
        
