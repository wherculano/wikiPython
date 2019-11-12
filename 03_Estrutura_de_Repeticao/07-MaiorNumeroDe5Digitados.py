"""
Faça um programa que leia 5 números e informe o maior número.
"""

numeros = [int(input(f'Digite o {i + 1}o numero: ')) for i in range(5)]

print(f'\nO maior numero digitado foi: {max(numeros)}')
