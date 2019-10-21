'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
n1, n2, n3 = tuple(map(int, input('Digite 3 numeros: ').split()))

maior = menor = n1
	
if n1 <= n2 >= n3:
	maior = n2
elif n1 >= n2 <= n3:
	menor = n2
if n1 <= n3 >= n2:
	maior = n3
elif n1 >= n3 <= n2:
	menor = n3
	
print(f'{maior} é o maior e {menor} é o menor.')
