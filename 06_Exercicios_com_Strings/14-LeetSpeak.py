"""
 Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo.
 A própria palavra leet admite muitas variações, como l33t ou '337.
 O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet,
 sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo.
 Pesquise sobre as principais formas de traduzir as letras.
 Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
 """

leet = {'a': '4', 'b': '!3', 'c': '(', 'd': '[)', 'e': '3',
        'f': 'pH', 'g': '6', 'h': '|-|', 'i': '!', 'j': '</', 'k': '|<',
        'l': '1', 'm': '|V|', 'n': '{\\}', 'o': '0', 'p': '|>', 'q': 'O,',
        'r': '|2', 's': '5', 't': '7', 'u': '[_]', 'v': '\\/', 'x': '><',
        'w': '\\X/', 'y': '`/', 'z': '2', }

frase = input('Digite uma frase: ').lower()
leet_frase = list(frase)

for indice, letra in enumerate(leet_frase):
    if letra in leet:
        leet_frase[indice] = leet[letra]

nova_frase = ''.join(leet_frase)
print(nova_frase)
