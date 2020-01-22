"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros.
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
"""


def ampm(hr, minuto):
    if hr <= 12:
        ap = 'A.M'
    else:
        ap = 'P.M'
    hr = hr if hr <= 12 else hr % 12

    def am_to_pm():
        return f'{hr}:{minuto} {ap}'

    return am_to_pm()


hora, minutos = list(map(int, input('Digite a hora e o minuto [hh:mm]: ').split(':')))
print(ampm(hora, minutos))
