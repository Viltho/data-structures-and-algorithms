import pytest

from CodeChallenge13.stackparanthesis import stackparanthesis

def test_stackparanthesis():
    actual = stackparanthesis("{}")
    expected = True
    assert actual == expected

def test_stackparanthesis():
    actual = stackparanthesis("{}(){}")
    expected = True
    assert actual == expected

def test_stackparanthesis():
    actual = stackparanthesis("()[[Extra Characters]]")
    expected = True
    assert actual == expected

def test_stackparanthesis():
    actual = stackparanthesis("(){}[[]]")
    expected = True
    assert actual == expected
    
def test_stackparanthesis():
    actual = stackparanthesis("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected
    
def test_stackparanthesis():
    actual = stackparanthesis("[({}]")
    expected = False
    assert actual == expected
    
def test_stackparanthesis():
    actual = stackparanthesis("(](")
    expected = False
    assert actual == expected
    
def test_stackparanthesis():
    actual = stackparanthesis("{(})")
    expected = False
    assert actual == expected
