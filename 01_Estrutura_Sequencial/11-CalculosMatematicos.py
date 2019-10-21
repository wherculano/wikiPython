'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''
n1 = int(input('n1 = '))
n2 = int(input('n2 = '))
n3 = float(input('n3 = '))

#pular uma linha
print()

#a
prod = (n1*2) * (n2/2)
print(f'a) {prod}')

#b
soma = (n1*3) + n3
print(f'b) {soma}')

#c
cubo = n3**3
print(f'c) {cubo}')
