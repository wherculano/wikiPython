'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
while True:
	try:
		n1 = float(input('\nDigite um numero: '))
		break
	except ValueError:
		print('Digite um NUMERO valido!')

print('Positivo' if n1 >= 0 else 'Negativo')
