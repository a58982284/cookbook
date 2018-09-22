def checkio(arry):
    if len(arry) ==0:
        return 0
    else:
        for i in range(len(arry)):
            if i % 2 ==0:
                sum += arry[i]
        return sum* arry[-1]
