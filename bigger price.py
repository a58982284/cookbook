from operator import itemgetter
rows = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
        ]
'''
rows_by_price = sorted(rows, key=itemgetter('price'),reverse=True)[:2]

print (rows_by_price)



def bigger_price(limit: int, data: list) -> list:
    rows_by_price = sorted(data,key=itemgetter('price'),reverse = True)[:limit]
    return rows_by_price
'''
def bigger_price(limit, data):
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]



#print (rows_by_price[0])
#print (rows_by_price)
