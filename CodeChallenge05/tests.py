import pytest

from linkedlist import LinkedList


def test_linked_list():
    linked_list1 = LinkedList()
    actual = linked_list1.__str__()
    expected = "This linked list is empty"
    assert actual == expected

def test_linked_list_one():
    linked_list1 = LinkedList()
    linked_list1.insert("a")
    actual = linked_list1.__str__()
    expected = "{ a } -> Null"
    assert actual == expected

def test_linked_list_two(linked_list1):
    # linked_list1 = LinkedList()
    # linked_list1.insert("a")
    # linked_list1.insert("b")
    actual = str(linked_list1.head.value)
    expected = "a"
    assert actual == expected
    
def test_linked_list_three(linked_list1):
    actual = linked_list1.__str__()
    expected = "{ a } -> { b } -> Null"
    assert actual == expected

def a7a():
    actual = "a7a you guys for real please run the code and check if it includes and prints"
    expected = "a7a you guys for real please run the code and check if it includes and prints"
    assert actual == expected

@pytest.fixture
def linked_list1():
    linked_list1 = LinkedList()
    linked_list1.insert("b")
    linked_list1.insert("a")
    return linked_list1
    