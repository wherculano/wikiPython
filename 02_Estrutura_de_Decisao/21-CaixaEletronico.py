"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

notas = [1, 5, 10, 50, 100]

while True:
	valor = int(input('Valor do Saque: R$'))
	if  valor < 10 or valor > 600:
		print('O valor deve estar entre R$10 e R$600.\n')
	else:
		for t in notas[::-1]:
			troco = valor // t
			print(f"{troco} notas de R${t}")
			valor %= t
		break
	