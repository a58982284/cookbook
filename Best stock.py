def best_stock(data):
    max_price = max(zip(data.values(),data.keys()))
    return max_price[1]


print (best_stock({'CAC': 10.0,'ATX': 390.2,'WIG': 1.2}))