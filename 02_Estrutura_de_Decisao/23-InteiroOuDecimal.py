"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento
"""

n = float(input('Digite um numero: '))

if n != round(n):
	print(f'{n} != {round(n)}')
	print('Numero Decimal')
else:
	print(f'{n} == {round(n)}')
	print('Numero Inteiro')
