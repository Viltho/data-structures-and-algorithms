import pytest
from CodeChallenge33.hashmap_left_join import left_join

dict1 = {
    "a": 1,
    "b": 3,
    "c": 2,
    "d": 3,
    "e": 5,
}

dict2 = {
    "b": 3,
    "d": 4,
    "e": 5
}

dict3 = {

}

dict4 = {
    "e": 5
}

def test_left_join_one():
    actual = left_join(dict1, dict2)
    expected = "{ a : 1 , Null } -> { b : 3 , 3 } -> { c : 2 , Null } -> { d : 3 , 4 } -> { e : 5 , 5 } -> None"
    assert expected == actual
     
def test_left_join_two():
    actual = left_join(dict1, dict3)
    expected = "{ a : 1 , Null } -> { b : 3 , Null } -> { c : 2 , Null } -> { d : 3 , Null } -> { e : 5 , Null } -> None"
    assert expected == actual
    
def test_left_join_three():
    actual = left_join(dict3, dict1)
    expected = "{  : None , None } -> None"
    assert expected == actual
    
def test_left_join_four():
    actual = left_join(dict2, dict4)
    expected = "{ b : 3 , Null } -> { d : 4 , Null } -> { e : 5 , 5 } -> None"
    assert expected == actual
    
def test_left_join_five():
    actual = left_join(dict2, dict1)
    expected = "{ b : 3 , 3 } -> { d : 4 , 3 } -> { e : 5 , 5 } -> None"
    assert expected == actual
    