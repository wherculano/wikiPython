'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

n1, n2, n3 = list(map(int,input('Digite os tres lados de um triangulo: ').split()))

if n1+n2 > n3 or n1+n3 > n2 or n2+n3 > n1:
	if n1 == n2 == n3  :
		print('Triangulo Equilatero')
	elif  n1 == n2 or n1==n3 or n2 == n3:
		print('Triangulo Isosceles')
	elif n1 != n2 != n3 :
		print('Triangulo Escaleno')
else:
	print('Nao é um Triangulo')
	