"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
from statistics import mean

notas = list(map(float, input('Notas [separadas por espaço]: ').split()))

print(f'\nNotas digitadas:\n{notas}')

#  media = sum(notas)/len(notas)
media = mean(notas)
print(f'\nMedia aritmética: {media:.2f}')
