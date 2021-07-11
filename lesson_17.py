try:
    div = 10 / 0
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por 0')

try:
    list = [1, 10]
    number = list[3]
except IndexError:
    print('Esse index não Existe')

try:
    x = '10' + 4
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

try:
    print('Codigo...')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa se não tiver Exception')

try:
    file = open('files/test.txt', 'r')
    text = file.read()
    a = '1'+ 1
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
finally:
    print('Finalizando Bloco')
    file.close()