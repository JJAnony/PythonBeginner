a = int(input('Entre com um numero:'))

isCousin = 0
for x in range(1, a + 1):
    if a % x == 0:
        isCousin += 1

if isCousin == 2:
    print('o numero {} é primo'.format(a))
else:
    print('o numero {} não é primo'.format(a))
