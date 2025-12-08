import math

class Junction_Box():
    def __init__(self, jid, x, y, z):
        self.jid = jid
        self.x = x
        self.y = y
        self.z = z

    def calculate_distance(self, other):
        return math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2 )

def is_connected(jid, connections):
    for i in connections:
        if jid in i:
            return True
        
    return False

def get_best_connection(distances, connections):
    #for distance in distances:
    #
    #    if not (is_connected(distance[0], connections) and is_connected(distance[1], connections)):
    #        return distance

    if len(distances) == 0:
        return False
    
    return distances[0]

def get_largest_circuits(connections):
    circuits = []

    for connection in connections:
        found = False
        for circuit in circuits:
            if connection[0] in circuit and connection[1] in circuit:
                found = True
                break

            elif connection[0] in circuit:
                circuit.append(connection[1])
                found = True
                break

            elif connection[1] in circuit:
                circuit.append(connection[0])
                found = True
                break

        if not found:
            circuits.append([connection[0], connection[1]])

    circuits = merge_circuits(circuits)
    return sorted([len(x) for x in circuits], reverse=True)

def merge_circuits(circuits):

    old_length = float("inf")
    while len(circuits) < old_length:
        old_length = len(circuits)
        new_circuits = []
        done = False
        for i, c1 in enumerate(circuits):
            if done: break
            for j, c2 in enumerate(circuits):
                if i <= j:
                    continue

                if is_overlapping(c1, c2):
                    overlap = list(set(c1 + c2))
                    
                    circuits.pop(i)
                    circuits.pop(j)

                    new_circuits.append(overlap)
                    new_circuits += circuits

                    done = True
                    break

        if not done:
            new_circuits = circuits

        circuits = new_circuits

    return circuits

def is_overlapping(circuit1, circuit2):
    for i in circuit1:
        if i in circuit2:
            return True
        
    return False

def p1(junction_boxes, connection_amount):
    
    distances = []
    for i in junction_boxes:
        for j in junction_boxes:
            if j.jid <= i.jid:
                continue

            distances.append(
                (i.jid, j.jid, i.calculate_distance(j))
            )

    distances.sort(key= lambda x: x[2])

    connections = []

    remaining_connections = connection_amount
    #while (best_connection := get_best_connection(distances, connections)) and remaining_connections > 0:
    while remaining_connections > 0:

        best_connection = distances[0]

        connections.append(
            (best_connection[0], best_connection[1])
        )
        distances.pop(0)
        remaining_connections -= 1

    largest_circuits = get_largest_circuits(connections)

    return largest_circuits[0] * largest_circuits[1] * largest_circuits[2]


junction_boxes = []

with open("8/input.txt", "r") as file:
    for jid, line in enumerate(file.readlines()):
        x, y, z = line.rstrip().split(",")
        junction_boxes.append(
            Junction_Box(jid, int(x), int(y), int(z))
        )

print( # too low
    p1(junction_boxes, 1000)
)

