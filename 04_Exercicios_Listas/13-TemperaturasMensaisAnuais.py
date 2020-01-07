"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

temperaturas = [float(input(f'Temperatura média do mes de {mes}: ')) for mes in meses]

media_anual = sum(temperaturas) / len(temperaturas)

print(f'\nA média anual foi de {media_anual:.2f} graus.')

print('\nTemperaturas acima da média:')
for t, m in zip(temperaturas, meses):
    if t > media_anual:
        print(f'{m:<9}: {t:.2f}graus.')
