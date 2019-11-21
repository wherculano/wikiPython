"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

candidatos = {'candidato 1': 0, 'candidato 2': 0, 'candidato 3': 0}

while True:
    try:
        eleitores = int(input('Total de eleitores: '))
        break
    except ValueError:
        print('Digite apenas números!\n')

for e in range(1, eleitores + 1):
    for i, c in zip(range(1, len(candidatos) + 1), candidatos.keys()):
        print(f'{[i]} - {c}')

    print('-=' * 11)
    voto = int(input(f'\nVoto do Eleitor {e}: '))
    print()
    print('-=' * 11)
    if voto == 1:
        candidatos['candidato 1'] = candidatos.get('candidato 1', 0) + 1
    elif voto == 2:
        candidatos['candidato 2'] = candidatos.get('candidato 2', 0) + 1
    elif voto == 3:
        candidatos['candidato 3'] = candidatos.get('candidato 3', 0) + 1
    else:
        print('Voto nao contabilizado!\n')
        print('-=' * 11)

print('Total de Votos:')
for c, v in candidatos.items():
    print(f'  {c}: {v}')
print('-=' * 11)
