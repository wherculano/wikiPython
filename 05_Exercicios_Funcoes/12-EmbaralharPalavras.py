"""
Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
independentemente de como foram digitados.
"""


def emb_palavra(palavra):
    nova_palavra = list(palavra)
    tam = len(palavra) - 1
    for i in reversed(range(0, tam)):
        for j in range(0, tam):
            nova_palavra[i], nova_palavra[j] = nova_palavra[j], nova_palavra[i]
    palavra = ''.join(nova_palavra).lower()
    return palavra


variavel = 'PyThOn'
print(variavel)
print(emb_palavra(variavel))
