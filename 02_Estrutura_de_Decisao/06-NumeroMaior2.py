'''
Faça um Programa que leia três números e mostre o maior deles.
'''
n1, n2, n3 = list(map(int, input('Digite 3 numeros: ').split()))

if n1 >= n2 and n1 >= n3:
	print(f'{n1} é maior')
elif n2 >= n1 and n2 >= n3:
	print(f'{n2} é maior')
elif n3 >= n2 and n3 >= n1:
	print(f'{n3} é maior')
elif n1 == n2 == n3:
	print(f'Os numeros sao iguais')
