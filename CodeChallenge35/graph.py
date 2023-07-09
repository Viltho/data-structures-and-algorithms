class Node:
    def __init__(self, position, value):
        self.position = position
        self.value = value

class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(self.num_nodes)]
        self.weight = [[] for _ in range(self.num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1.position].append(node2.position)
                self.weight[node1.position].append(weight)
                if not directed:
                    self.data[node2.position].append(node1.position)
                    self.weight[node2.position].append(weight)
            else:
                node1, node2 = edge
                self.data[node1.position].append(node2.position)
                if not directed:
                    self.data[node2.position].append(node1.position)
                    
    def __repr__(self):
        result ="N | connections"
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "\n{} : {}".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "\n{} : {}".format(i, nodes)
        return result
num_nodes = 9
node0 = Node(0, "abdullah")
node1 = Node(1, "abdullah shaghnubah")
node2 = Node(2, "mustafa")
node3 = Node(3, "amjad")
node4 = Node(4, "nawras")
node5 = Node(5, "abdulkareem")
node6 = Node(6, "abdulrahman")
node7 = Node(7, "sahm")
node8 = Node(8, "mohammad alsmadi")

edges = [
    (node0, node1, 50),
    (node0, node2, 40),
    (node2, node3, 50),
    (node2, node4, 30),
    (node1, node5, 20),
    (node1, node6, 10),
    (node6, node7, 25),
    (node3, node8, 35),
    ]

graph1 = Graph(num_nodes, edges, weighted=True)
print(graph1)

