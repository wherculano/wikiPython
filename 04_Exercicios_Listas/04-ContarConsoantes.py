"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
"""

# importa todas as letras minusculas do alfabeto
from string import ascii_lowercase

print(ascii_lowercase)
letras = [input(f'Digite o {c + 1}º caracter: ') for c in range(10)]

vogais = 'aeiou'

for c in letras:
    if c in ascii_lowercase and c.lower() not in vogais:
        print(f'Consoante: {c}')
