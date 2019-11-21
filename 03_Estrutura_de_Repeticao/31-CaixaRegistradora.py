"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 3.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
"""
cont = 1
total = 0.0

while True:
    print('-=' * 15)
    print('Lojas Tabajara'.center(30))
    print('-=' * 15)
    while True:
        while True:
            try:
                valor = float(input(f'Produto {cont}: R$'))
                break
            except ValueError:
                print('Digite apenas números!\n')
        cont += 1
        if valor == 0:
            cont = 1
            break

        total += valor

    print('-' * 30)
    print(f'Total: R${total:.2f}')
    print('-' * 30)
    dinheiro = float(input('Dinheiro: R$'))
    print('-' * 30)
    troco = dinheiro - total
    print(f'Troco: R${troco:.2f}')
