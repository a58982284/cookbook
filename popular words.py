'''
from collections import Counter

def popular_words(words: str, text:list,):
    words_counts =words.count(text)


    return words_counts



print(popular_words('When I was One I had just begun When I was Two I was nearly new',['i','was' 'three', 'near']))

#words_count['i']
'''
def popular_words(text,words):
    lowerwords = str.lower(text)
    splitted_words = lowerwords.split() #['I', 'am', 'alive']
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
    return answer



print (popular_words('When I was One I had just begun When I was Two I was nearly new',['i', 'was', 'three', 'near']))