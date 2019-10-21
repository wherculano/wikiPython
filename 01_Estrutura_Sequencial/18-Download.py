'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
mb = float(input('Tamanho do Arquivo: '))

mbps = float(input('Velocidade da internet: '))

tempo = mb * 8 / mbps

hr = round(tempo / 3600)
min = round((tempo - (hr*3600)) / 60)
seg = round(tempo % 60)

print(f'{mb}MB sera baixado em {hr}:{min}:{seg}')
