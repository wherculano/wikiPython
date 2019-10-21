'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
prod1, prod2, prod3 = list(map(float, input('Digite o preço de 3 produtos: ').split()))

menor = prod1

if prod1 >= prod2 <= prod3:
	menor = prod2
elif prod1 >= prod3 <= prod2:
	menor = prod3
	
print(f'R${menor:.2f} é o mais barato.')
