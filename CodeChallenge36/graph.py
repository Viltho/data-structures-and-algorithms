from CodeChallenge35.graph_test import Graph, Node

def flatten(lst):
    """this function flattens a nested list of items

    Args:
        lst (list): a list of nested lists

    Returns:
        list: flattened list of lists
    """
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

def breadth_first_graph(node):
    """this function is to draw the graph in a breadth-first manner which returns the graph in a nested lists form

    Args:
        node (node): the node to start traversing from

    Returns:
        None: If head is none
        list: list of graph elements in traversal breadth-first order
    """
    if node is None:
        return None
    for i in node.list_of_edges:
        print(i) 

# def depth_first_graph(node):
#     if node is None:
#         return None
#     stack = [node]  # Use a stack instead of a queue
#     result = []
#     while stack:
#         current = stack.pop()  # Pop the top item from the stack
#         if current is not None:
#             result.append(current.value)  # Add value to the result list
#             # Push non-None neighbors in reverse order to simulate depth-first order
#             for neighbor in reversed(current.next):
#                 stack.append(neighbor)
#     return result
    
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

# print(graph1.head.value)

print(breadth_first_graph(graph1))
# print(depth_first_graph(graph1.head))
