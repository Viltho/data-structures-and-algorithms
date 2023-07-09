import pytest
from CodeChallenge35.graph_test import Graph, Node


    
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
    graph1.add_edge(node1, node2)
    graph1.add_edge(node2, node3)
    graph1.add_edge(node2, node4)
    graph1.add_edge(node4, node5)
    return graph1