'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

a = int(input('Valor de A: '))
if a != 0:
	b = int(input('Valor de B: '))
	c = int(input('Valor de C: '))
	
	delta = b**2 - 4*a*c
	if delta < 0:
		print('\nA equação nao possui raizes reais.')
	elif delta == 0:
		print('\nA equação possui apenas uma raiz real.')
		x1 = (-b + delta**0.5) / (2*a)
		print(f'X\' = {x1}')
	else:
		print('\nA equação possui duas raizes reais.')
		x1 = (-b + delta**0.5) / (2*a)
		x2 = (-b - delta**0.5) / (2*a)
		print(f'X\' = {x1}\nX\" = {x2}')
else:
	print(f'\nA nao pode ser igual a {a}')
	