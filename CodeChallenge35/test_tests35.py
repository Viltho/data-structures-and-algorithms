import pytest
from CodeChallenge35.graph_test import Graph

@pytest.fixture
def create_graph():
    graph = Graph()
    node1 = graph.add("mohammad")
    node2 = graph.add("abdullah")
    node3 = graph.add("abdullah shagnubah")
    node4 = graph.add("mustafa")
    node5 = graph.add("nawras")
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node2, node4)
    graph.add_edge(node4, node5)
    return graph

def test_get_nodes(create_graph):
    graph = create_graph
    nodes = graph.get_nodes()
    assert len(nodes) == 5
    assert "mohammad" in nodes
    assert "abdullah" in nodes
    assert "abdullah shagnubah" in nodes
    assert "mustafa" in nodes
    assert "nawras" in nodes

def test_neighbors(create_graph):
    graph = create_graph
    node2 = graph.head.next[0]
    neighbors = graph.neighbors(node2)
    assert len(neighbors) == 2
    assert "abdullah shagnubah" in neighbors
    assert "mustafa" in neighbors

def test_size(create_graph):
    graph = create_graph
    assert graph.size() == 5

def test_add_edge(create_graph):
    graph = create_graph
    node1 = graph.head
    node5 = graph.head.next[0].next[1]
    graph.add_edge(node1, node5, weight=5)
    assert len(graph.list_of_edges) == 5
    assert graph.list_of_edges[4] == ["mohammad", "mustafa", 5]
