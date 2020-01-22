"""
Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""


def pos_neg(n):
    return 'P' if n > 0 else 'N'


while True:
    try:
        num = float(input('Numero: '))
        break
    except ValueError:
        print('Digite apenas números!')

print(pos_neg(num))
