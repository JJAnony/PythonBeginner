a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('o maior valor é {}'.format(a))
elif b > a and b > c:
    print('o maior valor é {}'.format(b))
else:
    print('o maior valor é {}'.format(c))
