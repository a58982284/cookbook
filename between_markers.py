def between_markers(text, begin, end):
    if begin in text:   #如果初始标记在字符串中，则将字符串开始下标设为初始标记后一位;如果没有初始标记则将开始下标设为0
        b = text.find(begin) + len(begin)
    else:
        b = 0
    if end in text:     #如果结束标记在字符串中，将结束下标设为结束标记位置；若不在，则设置结束下标为字符串结尾
        e = text.find(end)
    else:
        e = len(text)
    return text[b:e]