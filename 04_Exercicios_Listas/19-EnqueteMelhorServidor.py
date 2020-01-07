"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
'Qual o melhor Sistema Operacional para uso em servidores?'

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado p/ desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes
e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""

print('Qual o melhor Sistema Operacional para uso em servidores?')

SO = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

votos = []
while True:
    try:
        print('\033[1;34m-\033[m' * 20)
        for num, so in enumerate(SO, start=1):
            print(f'{num}- {so}')
        op = int(input("\033[1;31;40mResp.: \033[m"))
        if op == 0:
            break
        elif 7 > op > 0:
            votos.append(op)
        else:
            print('\033[1;33mOpcao invalida!\033[m')
    except ValueError:
        print('\033[1;33mValor invalido!\033[m')

mais_votado = max(votos, key=votos.count)

votos_vencedor = votos.count(mais_votado)

print('\nSistema Operacional   Votos   %')
print('-------------------   -----   ----')
for i, s in enumerate(SO):
    tot = votos.count(i + 1)
    print(f'{s:<19}{tot:>5}{tot / len(votos) * 100:>9.0f}%')
print('-------------------  -----')
print(f'Total\t{len(votos):>16}')

print(f''''\nO Sistema Operacional mais votado foi o {SO[mais_votado - 1]}, com {votos_vencedor} votos, correspondendo a
{votos_vencedor / len(votos) * 100:.2f}% dos votos.''')
