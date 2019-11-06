"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
perguntas = [
"Telefonou para a vítima?\n[S/N]: ",
"Esteve no local do crime?\n[S/N]: ",
"Mora perto da vítima?\n[S/N]: ",
"Devia para a vítima?\n[S/N]: ",
"Já trabalhou com a vítima?\n[S/N]: "
]

resp = 0

for p in perguntas:
	print(p,end='')
	op = input().upper()
	if op == 'S':
		resp+= 1

print('\nParticipacao no crime: ',end='')
if resp == 5:
	print('Culpado!')
elif 3 <= resp < 5:
	print('Cumplice!')
elif resp == 2:
	print('Suspeito!')
else:
	print('Inocente!')
