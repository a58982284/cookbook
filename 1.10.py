def dedupe(items):
    seen =set()
    for item in items:          #items=[1,5,2,1,9,1,5,10]
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
b=list(dedupe(a))
print (b)


def dedupe(items,key=None):
    seen =set() #set()可变集合
    for item in items:
        val = item if key is None else key(item)#处理数据，使之变成可以比较的格式，即把数据解构，其中key为解构函数，val为解构后的数据
        if item not in seen:
            yield item
            seen.add(item)