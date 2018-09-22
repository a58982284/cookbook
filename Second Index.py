def second_index(text, symbol):
    if text.count(symbol) < 2:           # 如果该字母在字符串中仅出现一次，则返回None
        return None
    first = text.find(symbol)            # 使用find方法找到该字母在字符串中第一次出现位置
    return text.find(symbol, first + 1)  # 将find方法起始位置设为字母第一次出现后一位，返回得到字母出现第二次位置