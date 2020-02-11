"""
Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

nome = input('Nome: ').upper()

for letra in range(len(nome), 0, -1):
    for l in range(letra):
        print(nome[l], end="")
    print()
