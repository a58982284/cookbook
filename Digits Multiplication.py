def checkio(number):
    result = 1
    for i in str(number):
        if i != '0':
            result *= int(i)
    return result

print(checkio(1234))