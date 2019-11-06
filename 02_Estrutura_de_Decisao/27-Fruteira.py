"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

peso_mor = float(input('Quantidade de Morangos (Kg): '))
peso_mac = float(input('Quantidade de Maçãs (Kg): '))
total_mor = total_mac = 0

if peso_mor > 5:
    total_mor += peso_mor * 2.20
else:
    total_mor += peso_mor * 2.5
if peso_mac > 5:
    total_mac += peso_mac * 1.5
else:
    total_mac += peso_mac * 1.8

total = total_mac + total_mor

print(f'Total a pagar por {peso_mor:.0f}Kg do Morango: R$ {total_mor:.2f}')
print(f'Total a pagar por {peso_mac:.0f}Kg do Maçã: R$ {total_mac:.2f}')
print(f'Total a pagar: R$ {total:.2f}')
