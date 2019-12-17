"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
num = [int(input(f'{i + 1}o Numero: ')) for i in range(10)]

print(num[::-1])

# num.reverse()
# print(num)
