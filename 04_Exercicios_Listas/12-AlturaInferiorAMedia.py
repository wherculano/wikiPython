"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa q determine quantos alunos c/ mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""
alunos = [[int(input('\nIdade: ')), float(input('Altura: '))] for i in range(30)]

soma_alturas = sum(list(map((lambda x: x[1]), alunos)))

media_alturas = soma_alturas / len(alunos)

# cria uma lista de alunos maiores de 13 anos e com altura menor que a media
# depois atribui o tamanho da lista à variável
resp = len(list(filter((lambda x: x[0] > 13 and x[1] < media_alturas), alunos)))

print(f'\nHá {resp} aluno(s) maior(es) de 13 anos com altura inferior a {media_alturas:.2f}')
