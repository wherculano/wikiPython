"""
Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor .
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
from random import choice

num_dados = list(range(1, 7))

sorteios = [choice(num_dados) for _ in range(100)]

for n in num_dados:
    print(f'O número {n} for sorteado {sorteios.count(n)} vezes.')
