# При помощи list comprehension и/или dict comprehension превратите  текст в словарь
# {'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_price_list = [elem.rstrip('р').split() for elem in PRICE_LIST.split('\n')]
dict_price_list = {key: int(value) for key, value in list_price_list}
print(list_price_list)
print(dict_price_list)
