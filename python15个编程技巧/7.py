#(7)让一个方程一次返回多个值
def get_a_string():
    a = "lee"
    b = 'is'
    c ='cool'
    return a,b,c
sentence = get_a_string()
(a,b,c) = sentence
print(a,b,c)