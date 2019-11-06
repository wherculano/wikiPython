"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia, mes, ano = list(map(int, input('dd/mm/aaaa: ').split('/')))

meses = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31,
6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11:  30,
12: 31}

if dia > 0 and  (0 < mes <= 12) and (dia <= meses[mes]):
	print(f'A data é valida!')
else:
	print('Data invalida!')
