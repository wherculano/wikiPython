"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

while True:
    try:
        qt_turmas = int(input('Quantidade de Turmas: '))
        break
    except ValueError:
        print('Digite apenas números!\n')

alunos = []

for t in range(1, qt_turmas + 1):
    while True:
        try:
            qt_alunos = int(input(f'Quantidade de alunos da {t}a turma: '))
            if 0 < qt_alunos <= 40:
                alunos.append(qt_alunos)
                break
            else:
                print('As turmas não podem ter mais de 40 alunos.\n')
        except ValueError:
            print('Digite apenas números!\n')

media = sum(alunos) / qt_turmas

print(f'\nMedia de {media:.2f} alunos por turma.')
