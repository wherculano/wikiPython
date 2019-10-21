'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

n1, n2 = list(map(int,input('Digite dois numeros: ').split()))

if n1 > n2:
	print(f'{n1} > {n2}')
elif n1 < n2:
	print(f'{n2} > {n1}')
else:
	print(f'{n1} = {n2}')
	