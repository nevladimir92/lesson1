phones = ["iphone Xs", "Samsung Galaxy S10", "Xiaomi mi8"]



product = {
    "name":"Iphone",
    "stock": 24,
    "price": 65422.1,
    'recomend': phones
}

print(product)

print(product['recomend'][1])
product['recomend'].append('Iphone 6')
print(product)

stock = [
{'name':'iphone Xs Plus', 'stock':24, 'price': 69000},
{'name':'Samsung', 'stock':14, 'price': 49000},
{'name':'Xiaomi Mi8', 'stock':42, 'price': 34000},
]
stock[0]['price'] += 10000
print(stock[0]['name'])
