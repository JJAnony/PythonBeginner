def letter_counter(words):
    amount = []
    for x in words:
        length = len(x)
        amount.append(length)
    return amount

def test():
    return 'teste'

if __name__ == '__main__':
    list = ['cachorro', 'gato']
    print(letter_counter(list))