from collections import Counter
def most_frequent(data: list) -> str:
    word_counts = Counter(data)
    a = word_counts.most_common(1)

    return a

print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))
def most_frequent(data):
    return max(data, key=data.count)