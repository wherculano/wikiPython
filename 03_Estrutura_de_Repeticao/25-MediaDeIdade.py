"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
while True:
    while True:
        try:
            pessoas = int(input('Ha quantas pessoas na turma: '))
            break
        except ValueError:
            print('Digite apenas números!\n')
    while True:
        try:
            idades = [int(input(f'Idade da {i}a pessoa: ')) for i in range(1, pessoas + 1) if i >= 0]
            break
        except ValueError:
            print('Digite apenas números!\n')
    break

media = sum(idades) / len(idades)

if media > 60:
    print('Turma idosa.')
elif 26 <= media <= 60:
    print('Turma adulta.')
else:
    print('Turma jovem.')
