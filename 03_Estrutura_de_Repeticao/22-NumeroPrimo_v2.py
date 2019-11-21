"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível.
"""

while True:
    try:
        n = int(input('Numero: '))
        aux = n
        if n < 0:
            n *= -1
        break
    except ValueError:
        print('Valor invalido!\n')

div = 1
divisores = []
for d in range(2, int(n // 2) + 1):
    if n % d == 0:
        div += 1
        divisores.append(d)

if div < 2:
    print(f'{aux} é primo')
else:
    print(f'{aux} nao é primo pois é divisivel por: ', end='')
    for i in divisores:
        print(i, end='')
        if i == divisores[-1]:
            print('.')
        else:
            print(', ', end='')
