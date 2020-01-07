"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

while True:
    try:
        resp = [input(f'{p}\n[S/N]: ')[0].upper() for p in perguntas]
        break
    except IndexError:
        print('Responda apenas S ou N meu caro!!')

tot = resp.count('S')
if tot == 2:
    print('Suspeito(a)!')
elif 2 < tot <= 4:
    print('Cumplice!!')
elif tot > 4:
    print('Assassino(a)!!!')
else:
    print('Inocente!')
