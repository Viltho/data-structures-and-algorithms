import pytest

from CodeChallenge17.breadthfirst import TreeNode, Node, BST

def test_bfs_empty_tree():
    x = TreeNode()
    actual = x.bfs(x.root)
    expected = []
    assert actual == expected

def test_bfs_positive():
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
    
    actual = tree1.bfs(tree1.root)
    expected = [1,5,4,2,6,3,9]
    assert actual == expected

def test_bfs_negative():
    tree1 = TreeNode()
    node1 = Node(-1)
    node2 = Node(-5)
    node3 = Node(2)
    node4 = Node(-2)
    node5 = Node(-6)
    node6 = Node(23)
    node7 = Node(-9)

    tree1.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    actual = tree1.bfs(tree1.root)
    expected = [-1,-5,2,-2,-6,23,-9]
    assert actual == expected

# def test_preorder(test_BST):
#     assert test_BST.preorder(test_BST.root) == [5,4,3,2,6,7,8]
# def test_inorder(test_BST):
#     assert test_BST.inorder(test_BST.root) == [2,3,4,5,6,7,8]
# def test_postorder(test_BST):
#     assert test_BST.postorder(test_BST.root) == [2,3,4,8,7,6,5]
# def test_contains(test_BST):
#     assert test_BST.contains(test_BST.root, 5) == True
# def test_contains_False(test_BST):
#     assert test_BST.contains(test_BST.root, 9) == False

# @pytest.fixture
# def test_BST():
#     tree1 = TreeNode()
#     node1 = Node(1)
#     node2 = Node(5)
#     node3 = Node(4)
#     node4 = Node(2)
#     node5 = Node(6)
#     node6 = Node(3)
#     node7 = Node(9)

#     tree1.root = node1
#     node1.left = node2
#     node1.right = node3
#     node2.left = node4
#     node2.right = node5
#     node3.left = node6
#     node3.right = node7
