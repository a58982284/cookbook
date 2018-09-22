#(13)找到数组中出现最多次的元素

test = [1,2,3,4,5,6,5,2,3,1,4,7,8,9,8,7,4,5,6,2,1]
print(max(set(test),key=test.count))