list_int = [1, 3, 5, 7]
list_animal = ['gato', 'cachorro', 'elefante']

print(sum(list_int))

print(list_animal[1])

for x in list_animal:
    print(x)

tuple_int = (1, 10, 12, 14)

print(tuple_int[2])
print(len(tuple_int))
print(len(list_animal))
tuple_animal = tuple(list_animal)
print(type(tuple_animal))
print(tuple_animal)