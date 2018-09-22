a = (1, 2, 3, 4, 5, 6, 7, 9)
b=tuple()

print (type((a[0],a[2],a[-2])))
print (b)

def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])

print (easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))