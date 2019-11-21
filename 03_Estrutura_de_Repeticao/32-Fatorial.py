"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

while True:
    try:
        fat = int(input('Fatorial de: '))
        break
    except ValueError:
        print('Digite apenas números!\n')
f = 1

print(f'{fat}! = ', end='')
for i in range(fat, 0, -1):
    print(f'{i}', end='')
    f *= i
    if i == 1:
        print(' = ', end='')
    else:
        print(' . ', end='')

print(f)
