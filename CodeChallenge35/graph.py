
class Node:
    def __init__(self, value):
        self.value = value
        self.weight = None
        self.next = []

class Graph:
    def __init__(self):
        self.list = []
        self.head = None
        self.directed = False
        self.weighted = False
        self.counter = 0
        
    def add(self, node):
        if self.head is None:
            self.head = node
        self.counter += 1
        self.list.append(node)
        
    def add_edge(self, node1, node2):
        node1.next.append(node2)
        return [(node.value, [node.value for node in node.next]) for node in self.list if node is not None]
    
    def get_nodes(self):
        if self.head is not None:
            return [node.value for node in self.list]
        else:
            return None

    def neighbors(self, node):
        if self.head is not None:
            for x in self.list:
                if node.value == x.value:
                    return [node.value for node in x.next]
                else:
                    pass
            return None
        else:
            return None
        
    def size(self):
        if self.head is not None:
            return self.counter
        else:
            return 0
            
            
graph1 = Graph()
node1 = Node("mohammad")
node2 = Node("abdullah")
node3 = Node("abdullah shagnubah")
node4 = Node("mustafa")
node5 = Node("nawras")
graph1.add(node1)
graph1.add(node2)
graph1.add(node3)
graph1.add(node4)
graph1.add(node5)
graph1.add_edge(node1, node2)
graph1.add_edge(node2, node3)
graph1.add_edge(node2, node4)
graph1.add_edge(node4, node5)
graph1.neighbors(node2)
print(graph1.size())