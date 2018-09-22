from dicttoxml import dicttoxml
m = {'a':1,'b':2,'c':3,'d':4}
xml = dicttoxml(m,custom_root='test',attr_type=False)
print(xml)