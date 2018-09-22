import re

text = "How are you? Eh, ok. Low or Lower? Ohhh."

a = re.findall(r'[A-Z]',text)

#print (a)

str4 = "".join(a)
print (str4)


def find_message(text: str) -> str:
    a = re.findall(r'[A-Z]',text)
    str1 = ''.join(a)
    return (str1)