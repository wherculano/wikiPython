'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
C = 5 * (F-32) / 9.
F = C * 9 / 5 + 32
'''
c = float(input('Graus Celcius: '))

f = c * 9 / 5 + 32

print(f'{c:.2f}C = {f:.2f}F')
