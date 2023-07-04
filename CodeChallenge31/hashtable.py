import re
from collections import Counter

def hashmap_repeated_word_nescafe(text):            
    words = re.findall(r"[a-zA-Z']+", text.lower())
    a, first_repeat = set(), ""
    word_counts = Counter(words)
    top_words = [word for word, count in word_counts.most_common(3)]
    for word in words:
        if word in a: 
            first_repeat = word
            return "top three words used are {},\n Set of all words: \n {},\n first repeat in the text is '{}'".format(top_words, word_counts, first_repeat)
        else: a.add(word)
    return "top three words used are {},\n Set of all words: \n {},\n first repeat in the text is '{}'".format(top_words, word_counts, first_repeat)

def hashmap_repeated_word(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    a, first_repeat = set(), ""
    for word in words:
        if word in a: 
            first_repeat = word
            return first_repeat
        else: a.add(word)

def hashmap_repeated_word_counter(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    a, first_repeat = set(), ""
    for word in words:
        if word in a: first_repeat = word
        else: a.add(word)
    word_counts = Counter(words)
    return word_counts

def hashmap_repeated_word_top_three(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    a, first_repeat = set(), ""
    for word in words:
        if word in a: first_repeat = word
        else: a.add(word.lower())
    word_counts = Counter(words)
    top_words = [word for word, count in word_counts.most_common(3)]    
    return top_words

text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

print(hashmap_repeated_word_nescafe(text))