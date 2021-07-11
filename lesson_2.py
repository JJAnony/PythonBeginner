a = int(input('Entre com um valor: '))
b = int(input('Entre com outro valor: '))
sum = a + b
subtraction = a - b
multiplication = a * b
division = a / b
rest = a % b

print(
    '\nResultado:\n'
    '\nSoma: {sum},'
    '\nSubitração: {sub},'
    '\nMultiplicação: {mult},'
    '\nDivisão: {div},'
    '\nResto: {rest}.'.format(
        sum=sum,
        sub=subtraction,
        mult=multiplication,
        div=division,
        rest=rest
    )
)
