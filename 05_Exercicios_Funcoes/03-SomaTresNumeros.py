"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""


def soma(a, b, c):
    return a + b + c


while True:
    try:
        x = float(input('Valor de x: '))
    except ValueError:
        x = 0
    try:
        y = float(input('Valor de y: '))
    except ValueError:
        y = 0
    try:
        z = float(input('Valor de z: '))
        break
    except ValueError:
        z = 0

print(soma(x, y, z))
