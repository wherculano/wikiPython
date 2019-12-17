"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = []
for a in range(10):
    soma = 0
    for n in range(4):
        nota = float(input(f'{n + 1}ª Nota do {a + 1}º aluno: '))
        soma += nota
    print('-=' * 12)
    medias.append(soma / 4)

# filtra a lista de médias e cria uma nova lista com medias maiores ou iguais a 7
cont = list(filter((lambda x: x >= 7), medias))

print(f'A quantidade de alunos com média maior ou igual a 7 é de: {len(cont)} aluno(s).')

