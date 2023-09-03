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

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes']= new_item['price']*.19
    return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Old list')
print(items)
