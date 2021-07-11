class Error(Exception):
    pass

class InputInvalidError(Error):
    def __init__(self, message):
        self.message = message



while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10:'))
        print(x)
        if x > 10 or x < 0:
            raise InputInvalidError('Número Invalido!')
        break
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas números.')
    except InputInvalidError as ex:
        print(ex.message)