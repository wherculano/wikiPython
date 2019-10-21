'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
vogais = ['a','e','i','o','u']

letra = input('Digite uma letra: ').lower()

if letra in vogais:
	print(f'"{letra.upper()}" é uma vogal.')
elif letra.isalpha():
	print(f'"{letra.upper()}" é uma consoante.')
else:
	print(f'"{letra}" nao é uma letra.')
