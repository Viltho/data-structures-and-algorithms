import pytest

from CodeChallenge13.stackparanthesis import stackparanthesis

def test_stackparanthesis():
    actual = stackparanthesis("{}")
    expected = True
    assert actual == expected

def test_stackparanthesis1():
    actual = stackparanthesis("{}(){}")
    expected = True
    assert actual == expected

def test_stackparanthesis2():
    actual = stackparanthesis("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_stackparanthesis3():
    actual = stackparanthesis("(){}[[]]")
    expected = True
    assert actual == expected
    
def test_stackparanthesis4():
    actual = stackparanthesis("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected
    
def test_stackparanthesis5():
    actual = stackparanthesis("[({}]")
    expected = False
    assert actual == expected
    
def test_stackparanthesis6():
    actual = stackparanthesis("(](")
    expected = False
    assert actual == expected
    
def test_stackparanthesis7():
    actual = stackparanthesis("{(})")
    expected = False
    assert actual == expected
