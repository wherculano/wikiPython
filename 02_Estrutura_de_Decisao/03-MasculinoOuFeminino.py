'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
while True:
	sexo = input('Informe seu sexo [M/F]: ').upper()
	if sexo == 'M':
		print('Masculino')
		break
	elif sexo == 'F':
		print('Feminino')
		break
	else:
		print('Sexo invalido!')
