def checkio(number: int) -> str:
    if number%3 == 0 and number%5==0:
        return 'Fizz Buzz'
    elif number%3==0 and number%5!=0:
        return 'Fizz'
    elif number%3 !=0 and number%5==0:
        return 'Buzz'
    else:
        return str(number)

print(checkio(15))
print(checkio(6))
print(checkio(5))
print(checkio(7))