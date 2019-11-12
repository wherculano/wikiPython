"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""
while True:
    try:
        base = int(input('Base: '))
        break
    except ValueError:
        print('Apenas NUMEROS!\n')

while True:
    try:
        exp = int(input('Expoente: '))
        break
    except ValueError:
        print('Apenas NUMEROS!\n')

print(f'{base}^{exp} = {base ** exp}')
