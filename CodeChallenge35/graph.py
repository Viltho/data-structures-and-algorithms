
class Node:
    """Node class with 3 variables value, weight, and next
    """
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
        """add function to add new node to the graph

        Args:
            node : a newly created node
        """
        if self.head is None:
            self.head = node
        self.counter += 1
        self.list.append(node)
        
    def add_edge(self, node1, node2):
        """adding a link that directly refers to the corresponding node

        Args:
            node1 (node): node 1 to be linked to node 2
            node2 (node): node 2

        Returns:
            list: list of nodes currently available in the graph
        """
        node1.next.append(node2)
        return [(node.value, [node.value for node in node.next]) for node in self.list if node is not None]
    
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
                    return [node.value for node in x.next]
                else:
                    pass
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
