"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

alunos = [(int(input(f'\nCódigo do {i}º aluno: ')), float(input('Altura: '))) for i in range(1, 10)]

maior = menor = alunos[0]

for k, v in alunos:
    if v > maior[1]:
        maior = (k, v)
    if v < menor[1]:
        menor = (k, v)

print(f'O aluno mais alto é o {maior[0]} com altura de {maior[1]:.2f}')
print(f'O aluno mais baixo é o {menor[0]} com altura de {menor[1]:.2f}')
