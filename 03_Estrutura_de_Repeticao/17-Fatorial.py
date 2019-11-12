"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

while True:
    try:
        fat = int(input('Fatorial de: '))
        break
    except ValueError:
        print('Valor Inválido!\n')

fatorial = 1

print('5!=', end='')

for f in range(fat, 0, -1):
    fatorial *= f
    print(f, end='')
    if f == 1:
        print('=', end='')
    else:
        print('.', end='')

print(fatorial)
