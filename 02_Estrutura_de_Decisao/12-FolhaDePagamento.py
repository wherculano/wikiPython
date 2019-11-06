'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Salário Bruto: (5 * 220)      : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)             : R$  110,00
        FGTS (11%)                  : R$  121,00
        Total de descontos     : R$  165,00
        Salário Liquido             : R$  935,00
'''

val_hr = float(input('Valor da Hora trabalhada: R$'))

qt_hr = int(input('Quantidade de Horas trabalhadas no mes: '))

sind = 3/100
fgts = 11/100
inss = 10/100
ir = liq = tot_desc = 0

bruto = val_hr * qt_hr

if bruto <= 900:
	tot_desc += (bruto * inss)
	liq = bruto - tot_desc
elif 900 < bruto <=1500:
	ir = 5/100
	tot_desc += (bruto * inss) +(bruto * ir)
	liq = bruto - tot_desc
elif 1500 < bruto <= 2500:
	ir = 10/100
	tot_desc += (bruto * inss) +(bruto * ir)
	liq = bruto - tot_desc
else:
	ir = 20/100
	tot_desc +=  (bruto * inss) +(bruto * ir)
	liq = bruto - tot_desc

print(f'''
Salário Bruto: ({val_hr} * {qt_hr})    : R$ {bruto:.2f}
(-) IR ({100*ir}%)                 : R$   {ir * bruto:.2f}
(-) INSS ( 10%)               : R$  {inss*bruto:.2f}
FGTS (11%)                  : R$  {fgts * bruto:.2f}
Total de descontos     : R$  {tot_desc:.2f}
Salário Liquido             : R$  {liq:.2f}
''')
