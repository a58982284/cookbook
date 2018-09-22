#(10)对数组内元素值和索引同时进行迭代

m = ['a','b','c','d']
for index,value in enumerate(m):
    print('{0}:{1}'.format(index,value))