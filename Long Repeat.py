def long_repeat(line):
    count = 0
    for char in line:
        while(line.count(char)>0):
