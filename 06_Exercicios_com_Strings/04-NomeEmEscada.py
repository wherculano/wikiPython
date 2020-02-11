"""
Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome = input('Nome: ').upper()

for letra in range(len(nome) + 1):
    for i in range(letra):
        print(nome[i], end="")
    print()
