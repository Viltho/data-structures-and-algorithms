import pytest
from CodeChallenge35.graph_test import Graph, Node
from CodeChallenge37.graph import BusinessTrip

def test_graph_functionality_onadd(test_graph):
    print(test_graph)
    
# def test_graph_functionality_onget(test_graph):
#     node1 = Node("issa")
#     node2 = Node("kareem")
#     node3 = Node("doha")
#     test_graph.add(node1)
#     test_graph.add(node2)
#     test_graph.add(node3)
#     assert test_graph.get_nodes() == ['mohammad', 'abdullah', 'abdullah shagnubah', 'mustafa', 'nawras', 'issa', 'kareem', 'doha']

# def test_graph_functionality_onedges(test_graph):
#     node = Node("abdullah")
#     assert test_graph.neighbors(node) == ['abdullah shagnubah', 'mustafa']
    
# def test_graph_functionality_oncount(test_graph):
#     node1 = Node("issa")
#     node2 = Node("kareem")
#     node3 = Node("doha")
#     test_graph.add(node1)
#     test_graph.add(node2)
#     test_graph.add(node3)
#     assert test_graph.size() == 8
    
# def test_graph_functionality_oncount():
#     graph1 = Graph()
#     assert graph1.list == []
    
@pytest.fixture
def test_graph():
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
    graph1.add_edge(node4, node5, 20)
    graph1.add_edge(node5, node2, 10)
    bt = BusinessTrip()
    return bt