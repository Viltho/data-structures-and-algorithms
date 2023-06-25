import pytest

from CodeChallenge30.hashtable import HashTable

def test_hashtable_testone():
    hash_table = HashTable()
    expected = 12
    actual = len(hash_table.item_list)
    assert expected == actual

def test_hashtable_add_new_item():
    hash_table = HashTable()
    hash_table.set_new_key_and_value("Abdullah", 30)
    expected = [["Abdullah", 30]]
    actual = hash_table.keys()
    assert expected == actual
    
def test_hashtable_multiple_add(test_HT):
    assert test_HT.keys() == [["Abdullah shaghnobah",28],["Abdullah",30],["Nawras",24], ["Amjad",26]]
    
def test_hashtable_has(test_HT):
    assert test_HT.has("Abdullah") == True
    
def test_hashtable_get(test_HT):
    assert test_HT.get("Abdullah") == 30
    
def test_hashtable_keys(test_HT):
    assert test_HT.keys_items() == ["Abdullah shaghnobah", "Abdullah", "Nawras", "Amjad"]

@pytest.fixture
def test_HT():
    hash_table = HashTable()
    hash_table.set_new_key_and_value("Abdullah", 30)
    hash_table.set_new_key_and_value("Amjad", 26)
    hash_table.set_new_key_and_value("Abdullah shaghnobah", 28)
    hash_table.set_new_key_and_value("Nawras", 24)
    return hash_table