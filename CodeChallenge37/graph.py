from CodeChallenge35.graph_test import Graph, Node

class BusinessTrip(Graph):
    def bfs(self, list_of_nodes, list):
        sum = 0
        status = False
        if len(list) == 0:
            return 0
        while len(list_of_nodes) > 0:
            if len(list_of_nodes) == 0 or len(list)== 0:
                if status:
                    return sum
                else:
                    return "Null"
            if list_of_nodes[0] == list[0][0] and list_of_nodes[1] == list[0][1]:
                sum += list[0][2]
                list_of_nodes.pop(0)
                status = True
            elif list_of_nodes[0] == list[0][0] and list_of_nodes[1] != list[0][1]:
                list.pop(0)
                status = False
            elif list_of_nodes[0] != list[0][0]:
                list.pop(0)
      

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
graph1.add_edge(node1, node2, 50)
graph1.add_edge(node2, node3, 40)
graph1.add_edge(node2, node4, 30)
graph1.add_edge(node4, node5, 10)
graph1.add_edge(node5, node2, 110)

newtrip = BusinessTrip()
print(newtrip.bfs(['nawras', 'abdullah', 'abddullah shagnubah'], graph1.list_of_edges))
# print(newtrip.bfs(['abdullah', 'abdullah shagnubah'], graph1.list_of_edges))
