"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos.
Para finalizar o conjunto de votos tem-se o valor zero.
"""

candidatos = {
    1: {'nome': 'Joao', 'votos': 0},
    2: {'nome': 'Jose', 'votos': 0},
    3: {'nome': 'Maria', 'votos': 0},
    4: {'nome': 'Antonio', 'votos': 0},
    5: {'nome': 'Voto Nulo', 'votos': 0},
    6: {'nome': 'Voto em Branco', 'votos': 0},
}

print(' ELEÇÃO PRESIDENCIAL '.center(40, '#'))

for k, v in candidatos.items():
    print(f"[{k}] - {v['nome']}")

print(' VOTE CONSCIENTE '.center(40, '#'))

while True:
    while True:
        try:
            voto = int(input('Voto: '))
            if voto == 0:
                break
            else:
                candidatos[voto]['votos'] += candidatos[voto].get(voto, 0) + 1
            break
        except (ValueError, KeyError):
            print('Opção Invalida!\n')
    if voto == 0:
        break

print()
print('-' * 25)
print('  CANDIDATO\tVOTOS ')
print('-' * 25)
for k, v in candidatos.items():
    print(f"{v['nome']:<17} {v['votos']}")

total_de_votos = sum([x['votos'] for x in candidatos.values()])

votos_nulos = candidatos[5]["votos"]
votos_brancos = candidatos[6]["votos"]

print('-' * 25)
print(f'{"Votos Nulos:":<16}{votos_nulos / total_de_votos * 100:.2f}% ')

print(f'{"Votos Brancos:":<16}{votos_brancos / total_de_votos * 100:.2f}% ')
print('-' * 25)
