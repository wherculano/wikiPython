'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
area = pi * raio^2
'''
from math import pi

raio = float(input('Raio: '))
area = pi * (raio**2)

print(f'Area = {area:.2f}')
