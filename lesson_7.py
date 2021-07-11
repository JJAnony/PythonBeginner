a = int(input('Nota primeiro bimestre: '))
while a > 10:
    a = int(input('Nota invalida. Entre com a nota correta: '))
b = int(input('Nota segundo bimestre: '))
while b > 10:
    b = int(input('Nota invalida. Entre com a nota correta: '))
c = int(input('Nota terceiro bimestre: '))
while c > 10:
    c = int(input('Nota invalida. Entre com a nota correta: '))
d = int(input('Nota quarto bimestre: '))
while d > 10:
    d = int(input('Nota invalida. Entre com a nota correta: '))

average = (a + b + c + d) / 4
print('Media: {}'.format(average))