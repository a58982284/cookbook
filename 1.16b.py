from itertools import compress

addresses = [
'5412 N CLARK' ,
'5148 N CLARK' ,
'5800 E 58TH' ,
'2122 N CLARK',
'5645 N RAVENSWOOD' ,
'1060 W ADDISON' ,
'4801 N BROADWAY' ,
'1039 W GRANVILLE' ,
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print (more5)
a = list(compress(addresses, more5)) #compress() 函数根据这个序列去选择输出对应位置为 True 的元素
b = compress(addresses, more5)  #迭代器
print (a)
print (b)