import pytest

from CodeChallenge15.tree import TreeNode, Node, BST

def test_empty_tree():
    x = BST()
    actual = x.root
    expected = None
    assert actual == expected

def test_tree_oneleaf():
    x = BST()
    x.Add(None, 5)
    actual = x.root.value
    expected = 5
    assert actual == expected

def test_tree_right_and_left():
    tree1 = BST()
    tree1.Add(None, 5)
    tree1.Add(tree1.root, 4)
    tree1.Add(tree1.root, 6)
    actual = tree1.inorder(tree1.root)
    expected = [4,5,6]
    assert actual == expected

def test_preorder(test_BST):
    assert test_BST.preorder(test_BST.root) == [5,4,3,2,6,7,8]
def test_inorder(test_BST):
    assert test_BST.inorder(test_BST.root) == [2,3,4,5,6,7,8]
def test_postorder(test_BST):
    assert test_BST.postorder(test_BST.root) == [2,3,4,8,7,6,5]
def test_contains(test_BST):
    assert test_BST.contains(test_BST.root, 5) == True
def test_contains_False(test_BST):
    assert test_BST.contains(test_BST.root, 9) == False

@pytest.fixture
def test_BST():
    tree1 = BST()
    tree1.Add(None, 5)
    tree1.Add(tree1.root, 4)
    tree1.Add(tree1.root, 6)
    tree1.Add(tree1.root, 3)
    tree1.Add(tree1.root, 2)
    tree1.Add(tree1.root, 7)
    tree1.Add(tree1.root, 8)
    return tree1
    
    
# def test_stackparanthesis4():
#     actual = stackparanthesis("{}{Code}[Fellows](())")
#     expected = True
#     assert actual == expected
    
# def test_stackparanthesis5():
#     actual = stackparanthesis("[({}]")
#     expected = False
#     assert actual == expected
    
# def test_stackparanthesis6():
#     actual = stackparanthesis("(](")
#     expected = False
#     assert actual == expected
    
# def test_stackparanthesis7():
#     actual = stackparanthesis("{(})")
#     expected = False
#     assert actual == expected

