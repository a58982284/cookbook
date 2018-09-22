def checkio(str_number, radix):
    try:                                     # 这里使用try是因为int容易引发一个ValueError使程序终止
        return int(str_number, radix)        #  python的int函数可以转换进制，第一位输入要转换的数字，第二位输入要转换的进制
    except ValueError:
        return -1