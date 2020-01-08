"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um
levantamento nas sucatas encontradas nesta área.
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada
um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo:
 - um número de identificação do mouse e o tipo de defeito:
 - necessita da esfera;
 - necessita de limpeza; necessita troca do cabo ou conector; quebrado ou inutilizado.

Uma identificação igual a zero encerra o programa.

Ao final o programa deverá emitir o seguinte relatório:

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

menu = ['necessita da esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']
situacao = []

while True:
    for i, m in enumerate(menu):
        print(f'{i}- {m}')
    try:
        opc = int(input('Opção: '))
        print('-' * 20)
        if opc == 0:
            break
        elif 1 <= opc <= len(menu):
            situacao.append(opc)
        else:
            print('Opção Inválida!\n')
    except ValueError:
        print('Valor invalido!\n')

print(f'\n{"Situação":^40}|{"Quantidade":^14}|{"Percentual":^14}|')
print('-'*70)
for i, s in enumerate(menu, start=1):
    quantidade = situacao.count(i)
    percentual = quantidade / len(situacao) * 100
    print(f'{i}- {s:<37}|{quantidade:^14}|{percentual:>10.2f} %')
