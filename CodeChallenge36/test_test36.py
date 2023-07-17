import pytest
from CodeChallenge36.queue import Node, Queue
from graph import Graph

@pytest.fixture
def graph():
    return Graph()

def test_add_node(graph):
    graph.add_node("A")
    assert graph.number_of_nodes == 1
    assert len(graph.dic_of_nodes) == 1
    assert len(graph.list_of_edges) == 1

def test_add_duplicate_node(graph):
    graph.add_node("A")
    result = graph.add_node("A")
    assert result == "this item already exists"

def test_add_edge(graph):
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 5)
    assert "B" in graph.list_of_edges["A"]
    assert "A" in graph.list_of_edges["B"]
    assert graph.list_of_edges["A"]["B"] == 5
    assert graph.list_of_edges["B"]["A"] == 5

def test_add_duplicate_edge(graph):
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", 5)
    result = graph.add_edge("A", "B", 10)
    assert result == "item already an edge"

def test_get_weight(graph):
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B", 5)
    graph.add_edge("B", "C", 10)
    graph.add_edge("C", "A", 15)
    weight = graph.get_weight(["A", "B", "C"])
    assert weight == 15

def test_get_weight_with_invalid_path(graph):
    graph.add_node("A")
    graph.add_node("B")
    weight = graph.get_weight(["A", "B", "C"])
    assert weight == "Null"

def test_breadth_first_traversal(graph):
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    result = graph.breadth_first_traversal("A")
    assert result == ["A", "B", "C", "D"]