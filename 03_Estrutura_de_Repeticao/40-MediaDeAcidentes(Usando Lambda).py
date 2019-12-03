"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
cidades = {
    1: {
        'codigo': 1, 'veiculos': 10000, 'acidentes': 100},
    2: {
        'codigo': 2, 'veiculos': 13000, 'acidentes': 10},
    3: {
        'codigo': 3, 'veiculos': 1100, 'acidentes': 230},
    4: {
        'codigo': 4, 'veiculos': 15000, 'acidentes': 10},
    5: {
        'codigo': 5, 'veiculos': 1900, 'acidentes': 70},
}

maior_indice = max(cidades.keys(), key=(lambda key: cidades[key]['acidentes']))

menor_indice = min(cidades.keys(), key=(lambda key: cidades[key]['acidentes']))

media_veiculos = sum([v['veiculos'] for v in cidades.values()]) / len(cidades)

acidentes = [v['acidentes'] for v in cidades.values() if v['veiculos'] < 2000]
media_acidentes = sum(acidentes) / len(acidentes)

print(f'''\nMaior indice de acidentes está na cidade {cidades[maior_indice]["codigo"]} com um total de
{cidades[maior_indice]["acidentes"]} acidentes''')

print(f'''\nMenor indice de acidentes está na cidade {cidades[menor_indice]["codigo"]} com um total de
{cidades[menor_indice]["acidentes"]} acidentes''')

print(f'\nMedia de veiculos nas {len(cidades)} é de {media_veiculos:.2f} carros por cidade.')

print(f'''\nMédia de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio é de:
{media_acidentes:.2f} acidentes por cidade.''')
