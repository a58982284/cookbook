def checkio(data):
    result = []
    for item in data:
        if data.count(item) > 1:
            result.append(item)
    return result