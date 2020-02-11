"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário
e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""
meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
         7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro', }

data = '29/10/1973'

dia, mes, ano = list(map(int, data.split('/')))

print(f'{dia} de {meses[mes]} de {ano}')
