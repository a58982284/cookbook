from collections import defaultdict

d= {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d =defaultdict(list)
for key,value in pairs:
    d[key].append(value)

