set_int = {1, 2, 3, 4, 5, 2}
print(set_int)

set_int_2 = {5, 6, 7, 8}
set_int_union = set_int.union(set_int_2)
print(set_int_union)

set_int_intersection = set_int.intersection(set_int_2)
print(set_int_intersection)

set_int_difference = set_int.difference(set_int_2)
set_int_difference_2 = set_int_2.difference(set_int)
print('1:', set_int_difference, '\n2:', set_int_difference_2)

set_int_symmetric_difference = set_int.symmetric_difference(set_int_2)
print(set_int_symmetric_difference)