"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e
o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

investido = 0
while True:
    try:
        cds = int(input('Quantos CDs possui: '))
        break
    except ValueError:
        print('Digite apenas números!\n')

for i in range(1, cds + 1):
    investido += float(input(f'Valor do {i}o CD: R$'))

valor_medio = investido / cds

print(f'\nValor investido: R${investido:.2f}.')
print(f'Gastou em media R${valor_medio:.2f} por CD.')
