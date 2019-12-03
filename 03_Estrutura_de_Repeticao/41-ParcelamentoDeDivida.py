"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""

valor = float(input('Valor: R$ '))
taxa = 0

print('Valor da Dívida|Valor dos Juros|Quantidade de Parcelas|Valor da Parcela')
for qt_parc in range(0, 13, 3):
    if qt_parc == 0:
        qt_parc = 1
    val_jur = valor * taxa / 100
    val_div = (val_jur + valor) / qt_parc if taxa != 0 else valor
    print(f'{valor + val_jur:^15.2f}|{val_jur:^15.2f}|{qt_parc:^22}|{val_div:^16.2f}')
    taxa += 5
    if taxa == 5:
        taxa = 10
