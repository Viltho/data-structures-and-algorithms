from CodeChallenge36.queue import Node, Queue
        
class Graph:
    def __init__(self, directed=False):
        self.number_of_nodes = 0
        self.dic_of_nodes = {}
        self.list_of_edges = {}
        self.directed = directed
        
        ### for weight calculation
        self.sum_of_weights = 0
        self.last_item = ""
        
        ### for breadth-first search
        self.visited = []
        self.bfs_list = {}
        self.queue = Queue()
    
    def add_node(self, value):
        if value in self.dic_of_nodes:
            return "this item already exists"
        else:
            self.number_of_nodes += 1
            node = Node(value)
            self.dic_of_nodes[value] = node
            self.list_of_edges[value] = {}
        
    def add_edge(self, node1, node2, weight=0):
        if node2 in self.list_of_edges[node1]:
            return "item already an edge"
        else:
            self.list_of_edges[node1].update({node2: weight})
            if not self.directed:
                self.list_of_edges[node2].update({node1: weight})
    
    def get_weight(self, list):
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
    
    # def depth_first_traversal(self,value):

            
graph = Graph()
graph.add_node("dammam")
graph.add_node("riyadh")
graph.add_node("mekkah")
graph.add_node("medinah")
graph.add_node("al-hassa")
graph.add_node("jeddah")
# print(graph.dic_of_nodes)

graph.add_edge("dammam", "riyadh", 400)
graph.add_edge("dammam", "al-hassa", 300)
graph.add_edge("riyadh", "mekkah", 800)
graph.add_edge("mekkah", "jeddah", 85)
graph.add_edge("jeddah", "medinah", 400)
graph.add_edge("mekkah", "medinah", 450)
# print(graph.list_of_edges['dammam'])
print(graph.get_weight(["medinah", "mekkah", "riyadh"]))
# print(graph.breadth_first_traversal("medinah"))
# print(graph.visited)
