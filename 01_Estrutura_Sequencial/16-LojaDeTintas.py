'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
from math import ceil

area = float(input('Area (m2): '))
litros = area / 3
latas = 1 if (litros / 18) <=1 else ceil(litros/18)
preco = 80 * latas

print(f'Litros: {litros:.2f}')
print(f'Quantidade de Latas: {latas}')
print(f'Total: R${preco:.2f}')
