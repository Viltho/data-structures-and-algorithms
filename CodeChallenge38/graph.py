from CodeChallenge36.queue import Node, Queue
from CodeChallenge10.stack import Stack
        
class Graph:
    def __init__(self, directed=False):
        """This is the constructor for Graph instances created.
        it contains all the variables needed to create a graph

        Args:
            directed (bool, optional): If set to true while 
            creating a graph it states that a node can point to one direction not the other. Defaults to False.
        """
        self.number_of_nodes = 0
        self.dic_of_nodes = {}
        self.list_of_edges = {}
        self.directed = directed
        
        ### for weight calculation
        self.sum_of_weights = 0
        self.last_item = ""
        
        ### for breadth-first and depth-first search
        self.visited = []
        self.bfs_list = {}
        self.queue = Queue()
        self.stack = Stack()
    
    def add_node(self, value):
        """this function is called when the node is added

        Args:
            value (string or integer): it sets a new node to the graph and returns nothing

        Returns:
            string: the only case this function would return is when you try adding the same node twice
        """
        if value in self.dic_of_nodes:
            return "this item already exists"
        else:
            self.number_of_nodes += 1
            node = Node(value)
            self.dic_of_nodes[value] = node
            self.list_of_edges[value] = {}
        
    def add_edge(self, node1, node2, weight=0):
        """adds an edge between two nodes and the default weight is zero for the link if not mentioned

        Args:
        node1 (str): The first node.
        node2 (str): The second node.
        weight (int, optional): The weight of the edge. Defaults to 0.

        Returns:
            str: A message indicating whether the edge already exists.
        """
        if node2 in self.list_of_edges[node1]:
            return "item already an edge"
        else:
            self.list_of_edges[node1].update({node2: weight})
            if not self.directed:
                self.list_of_edges[node2].update({node1: weight})
    
    def get_weight(self, list):
        """this method returns the weight of a certain path if it meets the criteria

        Args:
            list (a list of names): this list may contain a list of names of the nodes that is required to calculate the weight for

        Returns:
            sum : returns the weight of the given path if it meets the criteria
        """
        self.sum_of_weights = 0
        self.last_item = ""
        for item in list:
            if self.last_item == "":
                self.sum_of_weights += 0
            else:
                if item in self.list_of_edges[self.last_item]:
                    self.sum_of_weights += self.list_of_edges[self.last_item][item]
                else:
                    return "Null"
            self.last_item = item
        return self.sum_of_weights
    
    def breadth_first_traversal(self,value):
        """finding the nodes inside the graph using the given value/ starting from the given value and traversing the graph accordingly.

        Args:
            value (string or integer): this value is where the first traversal should start from.

        Returns:
            list: returns a list of the nodes in the graph
        """
        self.queue.enqueue(value)
        self.last_item = self.queue.front.value
        self.visited.append(self.last_item)
        while self.queue.front:
            for key in self.list_of_edges[self.last_item]:
                if key in self.visited:
                    pass
                else:
                    self.queue.enqueue(key)
                    self.visited.append(key)
                    
            self.queue.dequeue()
            if self.queue.front is not None:
                self.last_item = self.queue.front.value
        
        return self.visited
    
    def depth_first_traversal(self,value):
        """finding the nodes inside the graph using the given value/ starting from the given value and traversing the graph accordingly.

        Args:
            value (string or integer): this value is where the first traversal should start from.

        Returns:
            list: returns a list of the nodes in the graph
        """
        if not self.list_of_edges:
            return []
        self.visited=[]
        self.stack.push(value)
        while self.stack.top:
            current = self.stack.pop()
            if current not in self.visited:
                self.visited.append(current)
            for key in self.list_of_edges[current]:
                if key not in self.visited:
                    self.stack.push(key)
        return self.visited
        
# graph = Graph()
# graph.add_node("dammam")
# graph.add_node("riyadh")
# graph.add_node("mekkah")
# graph.add_node("medinah")
# graph.add_node("al-hassa")
# graph.add_node("jeddah")
# # print(graph.dic_of_nodes)

# graph.add_edge("dammam", "riyadh", 400)
# graph.add_edge("dammam", "al-hassa", 300)
# graph.add_edge("riyadh", "mekkah", 800)
# graph.add_edge("mekkah", "jeddah", 85)
# graph.add_edge("jeddah", "medinah", 400)
# graph.add_edge("mekkah", "medinah", 450)
# # print(graph.list_of_edges['dammam'])
# # print(graph.get_weight(["medinah", "mekkah", "riyadh"]))
# # print(graph.breadth_first_traversal("medinah"))
# # print(graph.visited)


# graph = Graph()
# graph.add_node("A")
# graph.add_node("B")
# graph.add_node("D")

# graph.add_node("C")
# graph.add_node("G")

# graph.add_node("E")
# graph.add_node("H")
# graph.add_node("F")

# graph.add_edge("A", "D")
# graph.add_edge("A", "B")
# graph.add_edge("B", "C")
# graph.add_edge("C", "G")
# graph.add_edge("D", "E")
# graph.add_edge("D", "H")
# graph.add_edge("D", "F")
# graph.add_edge("F", "H")
# print(graph.depth_first_traversal("A"))
