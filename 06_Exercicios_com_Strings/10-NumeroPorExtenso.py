"""
Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
"""

numeros = {1: 'um', 2: 'dois', 3: 'tres', 4: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze',
           12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito',
           19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
           80: 'oitenta', 90: 'noventa'}

num = 98
if (1 <= num <= 20) or (num == 30) or (num == 40) or (num == 50) or (num == 60) or (num == 70) or (num == 80) or (
        num == 90):
    print(numeros[num])
else:
    d, u = [i for i in str(num)]
    d += '0'
    print(f'{numeros[int(d)]} e {numeros[int(u)]}')
