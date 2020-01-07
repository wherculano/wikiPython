"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

while True:
    nome = input('Atleta: ')
    ordens = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
    if nome == '':
        print('Saindo....')
        quit()
    else:
        print()
        saltos = [float(input(f'{ordem} Salto: ')) for ordem in ordens]
        break

print('\nResultado final:')
print(f'Atleta: {nome}')
print('Saltos: ', end='')
for salto in saltos:
    print(f'{salto:.1f}', end='')
    if salto == saltos[-1]:
        break
    print(' - ', end='')

media = sum(saltos) / len(saltos)
print(f'\nMédia dos saltos: {media:.1f}m')
