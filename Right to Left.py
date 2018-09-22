def left_join(phrases):
    hehe = ','.join(phrases)
    return hehe.replace('right', 'left')

print (left_join(("left", "right", "left", "stop")))
print (type(left_join(("left", "right", "left", "stop"))))
print (left_join(("brightness wright",)))
print (left_join(("enough", "jokes")))
print (left_join(("bright aright", "ok")))
print (left_join(("enough", "jokes")))