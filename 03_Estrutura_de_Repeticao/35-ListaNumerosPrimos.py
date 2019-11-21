"""
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
while True:
    try:
        num = int(input('Numero: '))
        break
    except ValueError:
        print('Digite apenas números!\n')

primos = []
div = 1

for p in range(2, num + 1):
    for n in range(2, p // 2 + 1):
        if p % n == 0:
            div += 1
    if div <= 1:
        primos.append(p)
    div = 1

print(primos)
