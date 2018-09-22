import string
def checkio(wordstr):
    wordstr = wordstr.lower()   #将字符串小写化
    return max(string.ascii_lowercase, key=wordstr.count)   #string.ascii_lowercase表示字母串'abcdef··z'