from model.television import Television
from model.calculator import Calculator
from utils.words_util import letter_counter, test

if __name__ == '__main__':
    television = Television()
    print(television.on)
    television.power()
    print(television.on)

    calculator = Calculator()
    print(calculator.sum(12, 13))

    list = ['gato', 'cachorro', 'elefante']
    print(letter_counter(list))
    print(test())