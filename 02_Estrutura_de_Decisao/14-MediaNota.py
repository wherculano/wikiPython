'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
n1 = float(input('Digite a 1a nota: '))
n2 = float(input('Digite a 2a nota: '))

media = (n1+n2)/2
conceito = ''
status = ''

if media >= 9:
	conceito = 'A'
	status = 'APROVADO'
elif 7.5 <= media < 9:
	conceito = 'B'
	status = 'APROVADO'
elif 6 <= media < 7.5:
	conceito = 'C'
	status = 'APROVADO'
elif 4 <= media < 6:
	conceito = 'D'
	status = 'REPROVADO'
else:
	conceito = 'E'
	status = 'REPROVADO'
	

print(f'Média: {media}\nConceito: {conceito}\nStatus: {status}')
