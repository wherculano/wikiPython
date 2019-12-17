"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média).
Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""


def clear():
    from os import system, name
    if name == ' nt':
        system('cls')
    else:
        system('clear')


atleta = dict()
ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

nome = input('Atleta: ')

atleta[nome] = [float(input(f'{x}o Salto: ')) for x in range(1, 6)]

clear()

for k, v in atleta.items():
    print(f'Atleta: {k}\n')
    for o, s in zip(ordem, v):
        print(f'{o + " Salto:":<16}{s}m')

    maior = v.pop(v.index(max(v)))
    menor = v.pop(v.index(min(v)))
    media = sum(v) / len(v)
    print(f'\n{"Melhor Salto:":<14}{maior}m')
    print(f'{"Pior Salto:":<14}{menor}m')
    print(f'Média dos demais saltos: {media:.1f}m')
    print('\nResultado final:')
    print(f'{k}: {media:.1f}m')
