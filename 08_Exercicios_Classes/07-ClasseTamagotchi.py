"""
Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade. Métodos: Alterar Nome, Fome, Saúde e Idade;
Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi,
este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado,
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
"""
import os
import time


class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self._idade = 1
        self._fome = True
        self._saude = False
        self._alimentos = []
        print(f'\nOi, meu nome é {self.nome}\n<:3  )~\n')

    def stats(self):
        """Funcao que contem todas as funções"""

        def clear():
            """Função para limpar a tela"""
            if os.name == 'nt':
                time.sleep(4)
                os.system('cls')
            else:
                time.sleep(4)
                os.system('clear')

        def alterar_nome():
            """Alterar o nome do pet"""
            nome = input('Novo nome: ')
            self.nome = nome
            print(f'\nOi, meu novo nome é {self.nome}\n')

        def fome():
            """Saber se está com fome ou não."""
            if self._alimentos:
                print(f'<:3  )~\nNao esta com fome!')
            else:
                print(f'<:3  )~\nEstá com fome!')

        def saude():
            """Saber como está a saúde."""
            if self._saude is False and self._fome is True:
                print(f'A saúde do(a) {self.nome} nao está ok.')
            else:
                print(f'A saude do(a) {self.nome}  está ok.')

        def idade():
            """Descobrir a idade."""
            print(f'Eu tenho {self._idade} anos.\n<:3   )~\n')

        def alimentar():
            """Alimentar o pet digitando o nome de qualquer comida."""
            alimento = input(f'O que voce vai dar de comida para o {self.nome}?\nComida: ')
            if alimento not in self._alimentos:
                if alimento.isalpha():
                    self._alimentos.append(alimento)
                    self._fome = False
                    self._saude = True
                    print('Opa! Obrigado(a) (*-*)')
                else:
                    print('Eca! Isso nao é comida (x.x)')
            else:
                print(f'{self.nome} ja comeu {alimento} antes!')

        def remedio():
            """Caso a saude nao esteja bem, usando este metodo resolve."""
            self._saude = True
            print(f'Agora o {self.nome} está curado!\n')

        def humor():
            """Verifica o humor"""
            if self._fome is True and self._saude is False:
                print(f'{self.nome} está mal humorado (>.<)\n')
            elif self._fome is False and self._saude is False:
                print(f'{self.nome} está "de boa" (\'.\')\n')
            else:
                print(f'{self.nome} está feliz (^.^)\n')

        def ajuda():
            """Mostra os comandos disponíveis para serem executados."""
            print('\nOs comandos disponiveis sao:')
            for i in functions.keys():
                print(f'\t- {i}')
                time.sleep(1)

        sair = False
        while not sair:
            # dict de funcoes
            functions = {'alterar nome': alterar_nome, 'fome': fome, 'idade': idade, 'saude': saude,
                         'humor': humor, 'alimentar': alimentar, 'ajuda': ajuda, 'remedio': remedio}

            op = input('[Digite "ajuda" para saber os comandos]\n~(  8:> Comando: ').lower()
            if op in functions:
                # se a funcao existir, executa ela!
                functions[op]()
                clear()
            elif op == 'sair':
                print('Saindo...tchaaaau\n')
                break
            else:
                print('Comando nao encontrado!\n')


if __name__ == '__main__':
    nome = input('Qual o nome do seu Hamster?\nNome: ')
    mouse = Tamagotchi(nome)
    mouse.stats()
