"""
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

1. quantos espaços em branco existem na frase.
2. quantas vezes aparecem as vogais a, e, i, o, u.
"""

vogais = ['a', 'e', 'i', 'o', 'u']

frase = input('Frase: ').lower()
espacos = frase.count(' ')

for v in vogais:
    print(f'A vogal \"{v}\" apareceu {frase.count(v)} vezes na frase.')
print(f'Na frase há {espacos} espacos.')
