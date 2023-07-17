# let say that it in case of lower case


def word(word, dic):
    for key in word:
        if key not in dic:
            dic[key] = 1
        else:   
            return False
    return True
        
dic = {}
words = "mustaf"
print(word(words, dic))