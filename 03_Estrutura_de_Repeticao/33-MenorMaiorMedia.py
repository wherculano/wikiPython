"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
 de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

temp_list = []
while True:
    try:
        temp_list.append(float(input('Temperatura: ')))
        menor = min(temp_list)
        maior = max(temp_list)
        media = sum(temp_list) / len(temp_list)
    except ValueError:
        print('\nSaindo...')
        break

try:
    print(f'\nMenor temperatura: {menor:.2f}')
    print(f'Maior temperatura: {maior:.2f}')
    print(f'Media das temperaturas: {media:.2f}')
except NameError:
    exit()
