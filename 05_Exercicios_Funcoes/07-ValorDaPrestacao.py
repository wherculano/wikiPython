"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
O programa deverá então exibir o valor a ser pago na tela.
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado
um valor igual a zero para a prestação.
Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma.
Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""


def valorPagamento(prest, dia):
    multa = (3 / 100) * prest
    juros = (0.1 / 100) * prest * dia
    juros_multa = prest + juros + multa
    return juros_multa


prestacoes = []
while True:
    valor = float(input('Valor da Prestação: R$'))
    dias = int(input('Dias de atraso: '))

    pagar = valorPagamento(valor, dias)
    prestacoes.append(pagar)
    print(f'O valor atualizado da sua prestação é de R${pagar:.2f}')

    try:
        op = int(input('\nPara sair digite 0 ou ENTER para continuar: '))
    except ValueError:
        op = 1
    if op == 0:
        break

print(f'\nForam pagas {len(prestacoes)} prestações num total de R${sum(prestacoes):.2f}')
