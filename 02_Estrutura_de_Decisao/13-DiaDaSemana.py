'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
dias = {1:'Domingo', 2:'Segunda-feira', 3:'Terça-feira', 4:'Quarta-feira', 5:'Quinta-feira', 6:'Sexta-feira', 7:'Sabado'}

dia = int(input('Digite um numero [1/7]: '))

if dia in dias:
	print(dias[dia])
else:
	print('Valor invalido!')
