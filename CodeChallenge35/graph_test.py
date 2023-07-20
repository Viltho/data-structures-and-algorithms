
class Node:
    """Node class with 3 variables value, weight, and next
    """
    def __init__(self, value):
        self.value = value
        self.weight = None
        self.next = []

class Graph:
    def __init__(self, directed=False, weighted=False):
        self.head = None
        self.directed = directed
        self.weighted = weighted
        
        self.counter = 0
        self.list = []
        self.list_of_edges = {}
        self.edges_counter = 0
        
    def add(self, value):
        """add function to add new node to the graph

        Args:
            node : a newly created node
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        self.counter += 1
        self.list.append(node)
        return node
        
    def add_edge(self, node1, node2, weight=0):
        node1.next.append(node2)
        self.list_of_edges[self.edges_counter] = [node1.value, node2.value, weight]
        self.edges_counter += 1
    
    def get_nodes(self):
        """loops through the graph.list

        Returns:
            list: list of all the nodes in the graph
        """
        if self.head is not None:
            return [node.value for node in self.list]
        else:
            return None

    def neighbors(self, node):
        """checks whether the node has any neighbors connected to it or not

        Args:
            node (node): a specific node in the graph to check

        Returns:
            list: list of all the nodes in the node.next
        """
        if self.head is not None:
            for x in self.list:
                if node.value == x.value:
                    return [neighbour.value for neighbour in x.next]
            return None
        else:
            return None

        
    def size(self):
        """the counter function

        Returns:
            counter: returns the number of elements in the graph
        """
        if self.head is not None:
            return self.counter
        else:
            return 0
            
            
graph1 = Graph()
node1 = graph1.add("mohammad")
node2 = graph1.add("abdullah")
node3 = graph1.add("abdullah shagnubah")
node4 = graph1.add("mustafa")
node5 = graph1.add("nawras")
graph1.add_edge(node1, node2)
graph1.add_edge(node2, node3)
graph1.add_edge(node2, node4)
graph1.add_edge(node4, node5)
# print(graph1.list_of_edges)

