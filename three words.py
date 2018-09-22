def checkio(words):
    list1 =words.split()
    num = 0
    for i in list1:
        if i.isalpha():
            num += 1
        else:
            num = 0
        if num >= 3:
            return True

    return False

print(checkio("Hello World hello"))

print(checkio('1 2 3 4'))







'''
'让我们教机器人区分单词和数字。给你一个字符串，用空白（一个空格）分隔单词和数字。
 单词只包含字母。 您应该检查字符串是否包含三个字连续。
 例如，字符串“start 5 one two three 7 end”连续包含三个单词。'
'''