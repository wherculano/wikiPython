'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
altura = float(input('Altura: '))

peso_h = (altura * 72.7) - 58
peso_m = (altura * 62.1) - 44.7

print(f'Peso ideal para Homem: {peso_h:.2f}Kg')
print(f'Peso ideal para Mulher: {peso_m:.2f}Kg')
