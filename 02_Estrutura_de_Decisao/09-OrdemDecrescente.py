'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

n = [int(input(f'Digite o {x}º: ')) for x in range(1,4)]
print(sorted(n, reverse=True))
