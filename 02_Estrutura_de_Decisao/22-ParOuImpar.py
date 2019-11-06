"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""

n = int(input('Digite um numero: '))

if n % 2 ==0:
	print(f'{n} é um numero par.')
else:
	print(f'{n} é um numero impar.')
