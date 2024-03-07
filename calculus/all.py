lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

rotations = int(input("Entrez le nombre de rotations à droite : "))

try:
    lst = [int(x) for x in lst]
except ValueError:
    pass


print("Liste après la rotation à droite de {} éléments :".format(rotations), lst)

mon_dict: dict = {"Alice": 16, "Albert": 13, "Tom": 12, "Nono": 19, "Hugo": 20}
new_dict: dict = {}

for name, note in mon_dict.items():
    if note >= 15:
        new_dict[name] = note


print(new_dict)


products = {
    1: {'name': 'Apple', 'price': 1.99, 'quantity': 10},
    2: {'name': 'Banana', 'price': 0.99, 'quantity': 5},
    3: {'name': 'Orange', 'price': 1.49, 'quantity': 0},
    4: {'name': 'Betrave', 'price': 1.70, 'quantity': 7},
    5: {'name': 'Clémentine', 'price': 1.99, 'quantity': 0},
    6: {'name': 'Poire', 'price': 2.49, 'quantity': 8}
}

print(products)

zero_quantity_products = [product for product in products.values() if product['quantity'] == 0]
print(zero_quantity_products)
