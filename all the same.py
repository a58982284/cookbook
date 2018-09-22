str=[1,2,3,4,5]
def all_the_same(elements):
    if len(set(elements))>1:
        #print(set(elements))
        return False
    else:
        print(set(elements))
        return True

print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same([]))
print(all_the_same([1]))