"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 : 'A'
02 : 'B'
03 : 'C'
04 : 'D'
05 : 'E'
06 : 'E'
07 : 'D'
08 : 'C'
09 : 'B'
10 : 'A'
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
"""
gabarito = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'E',
    7: 'D',
    8: 'C',
    9: 'B',
    10: 'A',
}

alternativas = 'ABCDE'
alunos = dict()
questoes = dict()
cont = 1

while True:
    print(f'Aluno {cont}')
    alunos[cont] = {}
    for q in gabarito.keys():
        while True:
            try:
                alunos[cont][q] = input(f'Questao {q}: ').strip().upper()[0]
                while True:
                    if alunos[cont][q] not in alternativas:
                        print('Alternativa invalida!')
                        alunos[cont][q] = input(f'Questao {q}: ').strip().upper()[0]
                    else:
                        break
                break
            except  IndexError:
                print('Opcao invalida!')
    alunos[cont]['acertos'] = 0
    op = input('Novo aluno? [S/N]: ').upper()
    if op == 'N':
        break
    print()
    cont += 1

print()
for aluno, questao in alunos.items():
    for gab, resp in zip(gabarito.items(), questao.items()):
        if gab == resp:
            alunos[aluno]['acertos'] += 1

maior = menor = max(alunos.values(), key=(lambda x: x['acertos']))['acertos']
notas = 0
for a, n in alunos.items():
    if n['acertos'] > maior:
        menor = maior
        maior = n['acertos']
    elif n['acertos'] < maior:
        menor = n['acertos']

    notas += n['acertos']

    print(f"Aluno: {a} - Nota: {n['acertos']}")
    print('-=' * 10)

media = notas / len(alunos)
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Total de alunos: {len(alunos)}')
print(f'Media das notas: {media:.2f}')
