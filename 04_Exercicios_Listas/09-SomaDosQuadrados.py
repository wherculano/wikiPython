"""
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
a = [int(input(f'{n + 1}o Numero: ')) for n in range(10)]

soma = sum(list(map((lambda x: x ** 2), a)))

print(f'\nA soma dos quadrados dos elementos = {soma}')
