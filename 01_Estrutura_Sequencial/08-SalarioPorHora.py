'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''
val_hr = float(input('Valor da Hora trabalhada: R$'))
hr_mes = int(input('Horas trabalhadas no mes: '))

salario = val_hr * hr_mes

print(f'Salario: R${salario:.2f}')
