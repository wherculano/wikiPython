'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

val_hr = float(input('Valor da Hora trabalhada: R$'))

hr_mes = float(input('Horas trabalhadas no mes: '))

bruto = val_hr * hr_mes
ir = bruto * (11/100)
inss = bruto * (8/100)
sind = bruto * (5/100)
liq = bruto - ir - inss - sind

print(f'''
+ Salário Bruto : R${bruto:.2f}
- IR (11%) : R${ir:.2f}
- INSS (8%) : R${inss:.2f}
- Sindicato ( 5%) : R${sind:.2f}
= Salário Liquido : R${liq:.2f}
''')
