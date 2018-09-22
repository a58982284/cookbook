def checkio(numbers_array) -> list:
    a = sorted(numbers_array,key=abs)

    return a


print (checkio((-20, -5, 10, 15)))