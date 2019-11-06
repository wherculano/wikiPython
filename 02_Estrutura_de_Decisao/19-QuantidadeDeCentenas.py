"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

n = int(input("Digite um numero: "))

for i in range(2):
	if n >= 100:
		cent = n // 100
		print(f'{cent} centena(s)', end=' ')
		n %= 100
		if 0 < n <= 9:
			print('e ', end='')
	if n >= 10:
		dez = n // 10
		print(f'{dez} dezena(s)', end=' ')
		n %= 10
		if n > 0:
			print('e ', end='')
	if 0 < n <= 9:
		uni = n//1
		print(f'{uni} unidade(s)', end='.')
		break
