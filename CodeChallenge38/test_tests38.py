# CodeChallenge36/test_test36.py
import pytest
from CodeChallenge38.graph import Graph

def test_depth_first_traversal_single_node():
    graph = Graph()
    graph.add_node("A")
    assert graph.depth_first_traversal("A") == ["A"]

def test_depth_first_traversal_linear_graph():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    assert graph.depth_first_traversal("A") == ["A", "B", "C"]

def test_depth_first_traversal_complex_graph():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    graph.add_node("G")
    graph.add_node("H")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("C", "G")
    graph.add_edge("G", "H")
    
    assert graph.depth_first_traversal("A") == ["A", "C", "G", "H", "F", "B", "E", "D"]
