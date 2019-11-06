"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

opc = {'A': 'Alcool',  'G': 'Gasilina'}

val_a = 1.90
val_g = 2.50
total = 0

litros = float(input('Litros: '))
tipo = input('[A] - Alcool\n[G] - Gasolina\nOpcao: ').upper()


if tipo == 'A':
	if litros <= 20:
		total += (val_a - 0.03 * val_a ) * litros
	else:
		total += (val_a - 0.05 * val_a) * litros
elif tipo == 'G':
	if litros <= 20:
		total += (val_a - 0.04 * val_g) * litros
	else:
		total += (val_a - 0.06 * val_h) * litros
else:
	print('Apenas Alcool ou Gasolina')

if tipo == 'A' or tipo == 'G':
	print(f'{litros} litros de {opc[tipo]} = R${total:.2f}')
