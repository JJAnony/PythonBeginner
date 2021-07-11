set_int = {1, 2, 3}
set_int_2 = {1, 2, 3, 4, 5, 6}

is_subset = set_int.issubset(set_int_2)
print('1 é um subconjunto de 2: {}'.format(is_subset))

is_subset = set_int_2.issubset(set_int)
print('2 é um subconjunto de 1: {}'.format(is_subset))

list_animals = ['cachorro', 'cachorro', 'gato', 'gato', 'elefente']
set_animals = set(list_animals)
print(set_animals)
