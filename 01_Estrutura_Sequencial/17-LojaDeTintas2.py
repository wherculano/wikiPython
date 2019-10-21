'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

from math import ceil

area = float(input('Area (m2): '))

val_grande = 80
val_peq = 25

litros = area / 6

lata_grande = ceil(litros/18)

lata_peq = ceil(litros/3.6)

total_grande = lata_grande * val_grande
total_peq = lata_peq * val_peq

print(f'Para pintar {area:.2f}m2 sera necessario {litros:.2f}L de tinta.')

print()

print(f'{lata_grande} lata(s) 18L = R${total_grande:.2f}')
print('OU')
print(f'{lata_peq} lata(s) 3.6L = R${total_peq:.2f}')
print('OU')

qtd_g = ceil(litros//18)
resto = litros%18
qtd_peq = ceil(resto/3.6)

print(f'{qtd_g} de 18L')

print(f'{qtd_peq} de 3.6L')

total_misto = (qtd_g*val_grande)+(qtd_peq*val_peq)

print(f'Total: R${total_misto:.2f}')

print()

menor = min([total_grande,total_peq, total_misto])
print(f'Melhor opcao: R${menor:.2f}')
