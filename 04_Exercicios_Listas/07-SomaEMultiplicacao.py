"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

# para iterar sobre a lista
from functools import reduce

numeros = [int(input(f'{n + 1}o numero: ')) for n in range(5)]

soma = sum(numeros)
mult = reduce((lambda x, y: x * y), numeros)

print()
print(f'Soma: {soma}')
print(f'Multiplicaçao: {mult}')
print(f'Todos os numeros: {numeros}')
