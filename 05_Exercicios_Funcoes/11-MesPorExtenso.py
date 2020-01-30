"""
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""


def format_data(data):
    dd, mm, aaaa = list(map(int, data.split('/')))
    if (1 <= dd <= 31) and (1 <= mm <= 12):
        if mm == 2 and dd > 29:
            return 'Data inválida!'
        return f'{dd} de {meses[mm]} de {aaaa}'
    else:
        return 'Data inválida!'


meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
         7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro', }

# printando todos os dias e meses
for m in range(1, 14):  # colocando 1 mes a mais para verificar se dará data inválida
    for d in range(1, 33):  # colocando 1 dia a mais para verificar se dará data inválida
        print(format_data(str(d) + '/' + str(m) + '/2020'))
    print('-=' * 15)
