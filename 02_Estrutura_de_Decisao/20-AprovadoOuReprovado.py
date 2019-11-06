"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

n1, n2, n3 = list(map(float,input('Digite 3 notas: ').split()))

media = (n1+n2+n3) / 3

if media == 10:
	print(f'Aprovado com Distinção!\nMédia: {media:.2f}')
elif media >= 7:
	print(f'Aprovado!\nMédia: {media:.2f}')
else:
	print(f'Reprovado!\nMédia: {media:.2f}')
