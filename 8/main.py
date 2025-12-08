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
    return sorted(circuits, reverse=True)

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

    return len(largest_circuits[0]) * len(largest_circuits[1]) * len(largest_circuits[2]), distances, connections

def are_all_included(max_junction_box_id, connections):
    unpacked_connections = []
    for connection in connections:
        unpacked_connections.append(connection[0])
        unpacked_connections.append(connection[1])

    for i in range(max_junction_box_id+1):
        if i not in unpacked_connections:
            return False
        
    return True


def p2(junction_boxes, p1_distances, p1_connections):
    distances = p1_distances
    connections = p1_connections

    max_junction_box_id = max([jb.jid for jb in junction_boxes])

    circuit_amount = float("inf")
    last_connection = ()
    all_included = False
    while circuit_amount > 1 or not all_included:

        if len(distances) == 0:
            break

        best_connection = distances[0]

        connections.append(
            (best_connection[0], best_connection[1])
        )
        distances.pop(0)

        last_connection = (best_connection[0], best_connection[1])
        circuit_amount = len(get_largest_circuits(connections))
        all_included = are_all_included(max_junction_box_id, connections)

        print(f"max {len(distances)} connections remaining..., currently {circuit_amount} circuits")

    jbxs = []
    for jb in junction_boxes:
        if jb.jid in last_connection:
            jbxs.append(jb)

    return jbxs[0].x * jbxs[1].x

junction_boxes = []

with open("8/input.txt", "r") as file:
    for jid, line in enumerate(file.readlines()):
        x, y, z = line.rstrip().split(",")
        junction_boxes.append(
            Junction_Box(jid, int(x), int(y), int(z))
        )

p1_result, p1_distances, p1_connections = p1(junction_boxes, 1000)
print(
    p1_result
)

print(
    p2(junction_boxes, p1_distances, p1_connections)
)

