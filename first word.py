def first_word(text):
    text =text.replace('.',' ').replace(',',' ').strip(' ')
    #return  text.split()
    return text.split()[0]

if __name__ == '__main__':
    print (first_word("Hello.world,"))
    print (first_word("don't.touch,it,"))
    print (first_word(" a word "))
    print (first_word("... and so on ..."))