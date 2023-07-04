from CodeChallenge17.breadthfirst import TreeNode, Node

def create_first_tree():
    """Creates a tree node

    Returns:
        inorder: returns the inorder traverse of the tree
    """
    tree1 = TreeNode()
    node1 = Node(150)
    node2 = Node(100)
    node3 = Node(75)
    node4 = Node(125)
    node5 = Node(160)
    node6 = Node(175)
    node7 = Node(250)
    node8 = Node(200)
    node9 = Node(300)
    node10 = Node(350)
    node11 = Node(500)

    tree1.root = node1
    node1.left = node2 
    node1.right = node7
    node2.left = node3
    node2.right = node5
    node5.left = node4
    node5.right = node6
    node7.left = node8
    node7.right = node10
    node10.left = node9
    node10.right = node11
    return tree1.inorder(node1)

def create_second_tree():
    """Creates a tree node

    Returns:
        inorder: returns the inorder traverse of the tree
    """
    tree2 = TreeNode()
    node1 = Node(42)
    node2 = Node(100)
    node3 = Node(15)
    node4 = Node(125)
    node5 = Node(160)
    node6 = Node(175)
    node7 = Node(600)
    node8 = Node(200)
    node9 = Node(4)
    node10 = Node(350)
    node11 = Node(500)

    tree2.root = node1
    node1.left = node2 
    node1.right = node7
    node2.left = node3
    node2.right = node5
    node5.left = node4
    node5.right = node6
    node7.left = node8
    node7.right = node10
    node10.left = node9
    node10.right = node11
    return tree2.inorder(node1)

def tree_intersection(tree1, tree2):
    """checks for the intersection of two binary trees

    Args:
        tree1 (Binary tree): the inorder traversal of the first tree
        tree2 (Binary tree): the inorder traversal of the second tree

    Returns:
        set_of_commons: set of common items shared between the two trees
    """
    first_tree = tree1
    second_tree = tree2
    set_of_commons = set()
    for item in first_tree:
        if item in second_tree:
            set_of_commons.add(item)
        else:
            pass
    return set_of_commons
    ### if i use dictionary time and space will increase

print(tree_intersection(create_first_tree(), create_second_tree()))
    