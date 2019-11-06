"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

op = input("""
Qual operacao deseja realizar?
[+, -, *, /]: """)

res = None

try:
	operacoes = {'+':n1+n2, '-':n1-n2, '/':n1/n2,'÷': n1/n2, '*':n1*n2, 'x':n1*n2}
	res = operacoes.get(op, 'Opcao Invalida')
	print(f'\n{n1} {op} {n2} = {res}')
except ZeroDivisionError:
	print('\nNao ha divisao por 0!')

if res != None:
	if res % 2==0:
		print(f'\n{res} é um numero par.')
	else:
		print(f'\n{res} é um numero impar.')
	if res >=0:
		print(f'\n{res} é um numero positivo.')
	else:
		print(f'\n{res} é um numero negativo.')
	if res != round(res):
		print(f'\n{res} é um numero decimal.')
	else:
		print(f'\n{res} é um numero inteiro.')
