import functools

class Node():
    def __init__(self, name, outwards_connections):
        self.name = name
        self.outwards_connections = outwards_connections

    @functools.cache
    def discover(self, visited_dac, visited_fft):#, already_visited):

        if self.name == "out" and visited_dac and visited_fft:
            return 1
        
        #if self.name in already_visited:
        #    return 0
        
        #already_visited.append(self.name)

        if self.name == "dac":
            visited_dac = True

        elif self.name == "fft":
            visited_fft = True
        
        total = 0
        for connection in self.outwards_connections:
            other_node = nodes[connection]
            total += other_node.discover(visited_dac, visited_fft)#, already_visited.copy())

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
    nodes["you"].discover(True, True)#, [])
)

#dac_connections = nodes["dac"].discover(True, True, [])
#print(dac_connections)
#dac_connections = 6651

#fft_connections = nodes["fft"].discover(True, True)#, [])
#print(fft_connections)

print(
    nodes["svr"].discover(False, False)#, [])
)

