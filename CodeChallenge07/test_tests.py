import pytest

from CodeChallenge06.linkedlist import LinkedList


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

def test_linked_list_two():
    linked_list1 = LinkedList()
    linked_list1.insert("a")
    actual = str(linked_list1.head.value)
    expected = "a"
    assert actual == expected
    
def test_linked_list_three():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    actual = linked_list1.__str__()
    expected = "{ a } -> { b } -> { c } -> Null"
    assert actual == expected

def test_linked_list_append():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    actual = linked_list1.__str__()
    expected = "{ a } -> { b } -> { c } -> { a } -> Null"
    assert actual == expected

def test_linked_list_insert_before():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.insert_before("c", "D")
    actual = linked_list1.__str__()
    expected = "{ a } -> { b } -> { D } -> { c } -> { a } -> Null"
    assert actual == expected

def test_linked_list_insert_after():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.insert_before("c", "D")
    linked_list1.insert_after("D", "B")
    actual = linked_list1.__str__()
    expected = "{ a } -> { b } -> { D } -> { B } -> { c } -> { a } -> Null"
    assert actual == expected

def test_linked_list_delete():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.insert_before("c", "D")
    linked_list1.insert_after("D", "B")
    linked_list1.delete("D")
    actual = linked_list1.__str__()
    expected = "{ a } -> { b } -> { B } -> { c } -> { a } -> Null"
    assert actual == expected

def test_linked_list_delete():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.insert_before("c", "D")
    linked_list1.insert_after("D", "B")
    linked_list1.delete("D")
    linked_list1.delete("b")
    actual = linked_list1.__str__()
    expected = "{ a } -> { B } -> { c } -> { a } -> Null"
    assert actual == expected

def test_linked_list_kthelement():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.insert_before("c", "D")
    linked_list1.insert_after("D", "B")
    linked_list1.delete("D")
    linked_list1.kthfromend(2)
    actual = linked_list1.kthfromend(2)
    expected = "c"
    assert actual == expected

def test_linked_list_kthelement2():
    linked_list1 = LinkedList()
    linked_list1.insert("c")
    linked_list1.insert("b")
    linked_list1.insert("a")
    linked_list1.append("a")
    linked_list1.insert_before("c", "D")
    linked_list1.insert_after("D", "B")
    actual = linked_list1.kthfromend(3)
    expected = "B"
    assert actual == expected

# @pytest.fixture
# def linked_list1():
#     linked_list1 = LinkedList()
#     linked_list1.insert("c")
#     linked_list1.insert("b")
#     linked_list1.insert("a")
#     linked_list1.append("a")
#     linked_list1.insert_before("c", "D")
#     linked_list1.insert_after("D", "B")
#     return linked_list1
    