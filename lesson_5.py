a = int(input('Nota primeiro bimestre: '))
b = int(input('Nota segundo bimestre: '))
c = int(input('Nota terceiro bimestre: '))
d = int(input('Nota quarto bimestre: '))

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    average = (a + b + c + d) / 4
    print('Media: {}'.format(average))
else:
    print('Foi digitada uma nota errada')
