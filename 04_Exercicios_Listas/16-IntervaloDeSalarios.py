"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja,
um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

# como nao entendi direito, vou fazer com 10 vendedores apenas.

intervalos = [299, 399, 499, 599, 699, 799, 899, 999, 1000]

val_vendedores = [float(input(f'Venda bruta do vendedor {i + 1}: R$')) * 0.09 + 200 for i in range(10)]

tot = [0] * len(intervalos)

for v in val_vendedores:
    for i in intervalos:
        if v <= i and (v >= (i - 99)):
            tot[intervalos.index(i)] += 1
            break
        elif v >= 1000:
            tot[-1] += 1
            break

print(tot)
