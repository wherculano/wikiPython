'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * (F-32) / 9
F = C  / 5 * 9 + 32
'''

f = float(input('Temperatura em Farenheit: '))

c = 5 * (f-32) / 9

print(f'{f:.2f}F = {c:.2f}C')
