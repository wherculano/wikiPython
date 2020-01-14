"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
e identificar os usuários com maior espaço ocupado.
Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres.
A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
de forma a agilizar a execução do programa. A conversão de espaço ocupado em disco, de bytes para megabytes deverá ser
feita através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
"""


def bytes_to_megabytes(bytes):
    return bytes / (1024 ** 2)


espaco_total = 100  # 100% do espaço do disco
nomes_e_espacos = []

with open('usuarios.txt', 'r') as usuarios:
    info = ''.join(usuarios.readlines())
    nomes, esp = info.split()[::2], info.split()[1::2]

usuarios.close()

for n, e in zip(nomes, esp):
    mb = bytes_to_megabytes(int(e))
    nomes_e_espacos.append((n, mb))

espaco_usado = sum([e[1] for e in nomes_e_espacos])

with open('relatorio.txt', 'a+') as relatorio:
    relatorio.write("""
ACME Inc.   Uso do espaco em disco pelos usuarios
------------------------------------------------------------------------
Nr.  Usuario        Espaco utilizado     % do uso\n\n""")

    for i, n in enumerate(nomes_e_espacos, start=1):
        espaco_percent = n[1] / espaco_usado * espaco_total
        relatorio.write(f'{i:<3} {n[0]:<15}{n[1]:>10.2f} MB {espaco_percent:>15.2f}%\n')

relatorio.close()
