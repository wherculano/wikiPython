"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""


def digits(num):
    return len(str(num))


print(f'O numero 100 tem {digits(100)} digitos')
print(f'O numero 1000 tem {digits(1000)} digitos')
print(f'O numero 100000 tem {digits(100000)} digitos')
