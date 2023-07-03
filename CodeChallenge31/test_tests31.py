import pytest
from collections import Counter 

from CodeChallenge31.hashtable import hashmap_repeated_word, hashmap_repeated_word_top_three, hashmap_repeated_word_counter, hashmap_repeated_word_nescafe

def test_hashmap_repeated_word_testone():
    text = "Once upon a time, there was a brave princess who..."
    hash_table = hashmap_repeated_word(text)
    expected = 'a'
    actual = hash_table
    assert expected == actual

def test_hashmap_repeated_word_testtwo():
    text = "Once upon a time, there was a brave princess who..."
    hash_table = hashmap_repeated_word_counter(text)
    expected = Counter({'a': 2, 'once': 1, 'upon': 1, 'time': 1, 'there': 1, 'was': 1, 'brave': 1, 'princess': 1, 'who': 1})
    actual = hash_table
    assert expected == actual
    
def test_hashmap_repeated_word_testthree():
    text = "Once upon a time, there was a brave princess who..."
    hash_table = hashmap_repeated_word_top_three(text)
    expected = ['a', 'once', 'upon']
    actual = hash_table
    assert expected == actual
    
# ---------------------------------------------------------------
    
def test_hashmap_repeated_word_two_testone():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    hash_table = hashmap_repeated_word(text)
    expected = 'it'
    actual = hash_table
    assert expected == actual

def test_hashmap_repeated_word_two_testtwo():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    hash_table = hashmap_repeated_word_counter(text)
    expected = Counter({'the': 14, 'of': 12, 'was': 11, 'it': 10, 'we': 4, 'times': 2, 'age': 2, 'epoch': 2, 'season': 2, 'had': 2, 'before': 2, 'us': 2, 'were': 2, 'all': 2, 'going': 2, 'direct': 2, 'in': 2, 'period': 2, 'its': 2, 'for': 2, 'best': 1, 'worst': 1, 'wisdom': 1, 'foolishness': 1, 'belief': 1, 'incredulity': 1, 'light': 1, 'darkness': 1, 'spring': 1, 'hope': 1, 'winter': 1, 'despair': 1, 'everything': 1, 'nothing': 1, 'to': 1, 'heaven': 1, 'other': 1, 'way': 1, 'short': 1, 'so': 1, 'far': 1, 'like': 1, 'present': 1, 'that': 1, 'some': 1, 'noisiest': 1, 'authorities': 1, 'insisted': 1, 'on': 1, 'being': 1, 'received': 1, 'good': 1, 'or': 1, 'evil': 1, 'superlative': 1, 'degree': 1, 'comparison': 1, 'only': 1})
    actual = hash_table
    assert expected == actual
    
def test_hashmap_repeated_word_two_testthree():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    hash_table = hashmap_repeated_word_top_three(text)
    expected = ['the', 'of', 'was']
    actual = hash_table
    assert expected == actual
    
# ---------------------------------------------------------------

def test_hashmap_repeated_word_three_testone():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    hash_table = hashmap_repeated_word(text)
    expected = 'summer'
    actual = hash_table
    assert expected == actual

def test_hashmap_repeated_word_three_testtwo():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    hash_table = hashmap_repeated_word_counter(text)
    expected = Counter({'was': 2, 'summer': 2, 'the': 2, 'i': 2, 'it': 1, 'a': 1, 'queer': 1, 'sultry': 1, 'they': 1, 'electrocuted': 1, 'rosenbergs': 1, 'and': 1, 'didn': 1, 't': 1, 'know': 1, 'what': 1, 'doing': 1, 'in': 1, 'new': 1, 'york': 1})
    actual = hash_table
    assert expected == actual
    
def test_hashmap_repeated_word_three_testthree():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    hash_table = hashmap_repeated_word_top_three(text)
    expected = ['was', 'summer', 'the']
    actual = hash_table
    assert expected == actual