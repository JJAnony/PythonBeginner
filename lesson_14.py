letter_counter = lambda list: [len(x) for x in list]

calculator = {
    'sum': lambda a, b: a + b,
    'subtraction': lambda a, b: a - b,
    'multiplication': lambda a, b: a * b,
    'division': lambda a, b: a / b
}

if __name__ == '__main__':
    list_animals = ['cachorro', 'gato', 'elefante']
    print(letter_counter(list_animals))

    print(type(calculator))

    sum = calculator['sum']
    print(sum(5, 10))
    subtraction = calculator['subtraction']
    print(subtraction(25, 18))
    multiplication = calculator['multiplication']
    print(multiplication(10, 5))
    division = calculator['division']
    print(division(100, 5))
