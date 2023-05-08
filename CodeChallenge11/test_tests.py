import pytest

from CodeChallenge11.pseudoqueue import PseudoQueue

def test_pseudo_queue_enqueue():
    pq = PseudoQueue()
    pq.enqueue("A")
    pq.enqueue("B")
    pq.enqueue("C")
    expected = "{ C } -> { B } -> { A } -> Null"
    actual = str(pq.stack1)
    assert actual == expected

def test_pseudo_queue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("A")
    pq.enqueue("B")
    pq.enqueue("C")
    pq.dequeue()
    expected = "{ B } -> { C } -> Null"
    actual = str(pq.stack2)
    assert actual == expected

# def test_pseudo_queue_dequeue():
#     pq = PseudoQueue()
#     pq.enqueue("A")
#     pq.enqueue("B")
#     pq.enqueue("C")
#     pq.dequeue()
#     expected = "{ B } -> { C } -> Null"
#     actual = str(pq.stack2)
#     assert actual == expected

def test_pseudo_queue_check_dequeued():
    pq = PseudoQueue()
    pq.enqueue("A")
    pq.enqueue("B")
    pq.enqueue("C")
    expected = "A"
    actual = pq.dequeue()
    assert actual == expected
    