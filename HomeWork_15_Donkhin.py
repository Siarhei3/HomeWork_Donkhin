import json

dict = {}
while True:
    product = input("Введите название продукта, если вы передумали нажмите 'стоп':")
    if product == 'стоп':
        break
    coast = float(input("Введите стоимоть товара, если вы передумали нажмите 'стоп':"))
    if coast == 'стоп':
        break
    dict.setdefault(product,coast)
with open('prod.json','w', encoding='UTF-8') as file:
    json.dump(dict, file, ensure_ascii=False)


