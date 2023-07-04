import pytest
from CodeChallenge17.breadthfirst import TreeNode, Node
from CodeChallenge32.tree_intersection import tree_intersection

def test_tree_intersection_one(test_BST, test_BST2):
    assert tree_intersection(test_BST, test_BST2) == {160, 100, 200, 175, 500, 125, 350}
    
def test_tree_intersection_one(test_BST2, test_BST3):
    assert tree_intersection(test_BST2, test_BST3) == {4}
    
def test_tree_intersection_one(test_BST3, test_BST4):
    assert tree_intersection(test_BST3, test_BST4) == set()
    
@pytest.fixture
def test_BST():
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

@pytest.fixture
def test_BST2():
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
    
@pytest.fixture
def test_BST3():
    tree1 = TreeNode()
    node1 = Node(1)
    node2 = Node(5)
    node3 = Node(4)
    node4 = Node(2)
    node5 = Node(6)
    node6 = Node(3)
    node7 = Node(9)

    tree1.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    return tree1.inorder(node1)

@pytest.fixture
def test_BST4():
    tree1 = TreeNode()
    return tree1.inorder(tree1.root)
