'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota_1 = float(input('1o Bimestre: '))
nota_2 = float(input('2o Bimestre: '))
nota_3 = float(input('3o Bimestre: '))
nota_4 = float(input('4o Bimestre: '))

media = (nota_1+nota_2+nota_3+nota_4)/4

print()
print(f'Media: {media:.2f}')
