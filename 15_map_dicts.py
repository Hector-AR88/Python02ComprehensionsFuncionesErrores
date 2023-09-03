items = [
    {
        'product_name': 'camisa',
        'price': 100,
    },
    {
        'product_name': 'pantalones',
        'price': 300
    },
    {
        'product_name': 'zapatos',
        'price': 200
    }
]
print(items)

prices = list(map(lambda item: f"Price: {item['price']}", items))
print(prices)

def add_taxes(item):
    item['taxes']= item['price']*.19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
