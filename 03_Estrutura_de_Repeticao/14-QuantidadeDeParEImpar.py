"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""
while True:
    try:
        numeros = [int(input(f'{i}o numero: ')) for i in range(1, 11)]
        break
    except ValueError:
        print('Valor invalido!\n')

par = imp = 0

for i in numeros:
    if i % 2 == 0:
        par += 1
    else:
        imp += 1

print(f'\nForam digitados {par} numeros pares e {imp} numeros impares.')
