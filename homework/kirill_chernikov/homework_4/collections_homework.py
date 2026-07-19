my_dict = dict()

my_dict['tuple'] = (1, 2, 3, 4, 5, 'tuple_string')
my_dict['list'] = [1, 2, 3, 4, 5, 'list_string']
my_dict['set'] = {1, 2, 3, 4, 5, 'set_string'}
my_dict['dict'] = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 'dict_string'
}

# Для того, что хранится под ключом ‘tuple’:
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
my_dict['list'].append(29)
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
my_dict['dict']['i am tuple'] = (1,)
my_dict['dict'].pop('dict_string', None)

# Для того, что хранится под ключом ‘set’:
my_dict['set'].add(90)
my_dict['set'].remove(3)

print(my_dict)
