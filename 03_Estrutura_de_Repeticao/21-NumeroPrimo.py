"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
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

div = 1  # se houver mais do que 2 divisores, entao nao é primo.

for d in range(2, n // 2 + 1):
    # n//2 pois nao existe divisor que seja maior do que a metade do proprio numero
    if n % d == 0:
        div += 1

if div > 1:
    print(f'{aux} nao é primo')
else:
    print(f'{aux} é primo')
