"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
num = []
while True:
    try:
        n = int(input(f'{len(num) + 1}o Numero: '))
        if n == 1:
            break
        num.append(n)
    except ValueError:
        print('\nValor Invalido!\n')

print(f'Foram digitados {len(num)} numeros.\n')

for n in num:
    print(n, end=' ')

print()
for n in num[::-1]:
    print(n)

print(f'\nA soma de todos os valores é igual a: {sum(num)}.\n')

media = sum(num) / len(num) if len(num) != 0 else 0
print(f'A media dos valores é igual a: {media:.2f}.\n')

acima_da_media = len(list(filter((lambda x: x > media), num)))
print(f'Quantidade de valores acima da média: {acima_da_media}.\n')

abaixo_de_7 = len(list(filter((lambda x: x < 7), num)))
print(f'Quantidade de valores abaixo de 7: {abaixo_de_7}.\n')

print(' FIM '.center(20, '#'))
