def index_power(arry,n):

    if len(arry) <= n:

        return -1


    else:
        sum = arry[n] ** n
        return sum

print(index_power([1, 2, 3, 4],2))




