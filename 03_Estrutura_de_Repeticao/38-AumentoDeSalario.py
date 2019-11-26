"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
from datetime import datetime

hoje = datetime.now().year  # ano atual

while True:
    try:
        salario = float(input('Salario: R$'))
        break
    except ValueError:
        print('Valor inválido!\n')

taxa_aum = 0.015

novo_salario = salario * (1 + taxa_aum)

for s in range(1997, hoje + 1):
    taxa_aum *= 2
    novo_salario += salario * (1 + taxa_aum)

print(f'O salario atual é de R${novo_salario:.2f}')
