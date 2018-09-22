'''
str = "runoob"
#print(str.capitalize())
#name = input('')
#print (str.endswith('.'))

if str.endswith('.'):
    print (str.capitalize())
else:
    print (str.capitalize()+ '.')
'''

def correct_sentence(str):
    if str.endswith('.'):
        return str.capitalize()
    else:
        return str.capitalize() + '.'


def correct_sentence1(text: str) -> str:
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'

    return text


if __name__ == '__main__':
    #print("Example:")
    print(correct_sentence("Welcome to new york"))
    print(correct_sentence1("Welcome to new york"))