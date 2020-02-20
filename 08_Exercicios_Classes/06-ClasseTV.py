"""
Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
"""


class TV:
    def __init__(self):
        self._canal = 1
        self._volume = 1

    @property
    def volume(self):
        '''retorna volume atual'''
        return self._volume

    @property
    def canal(self):
        '''retorna o canal atual'''
        return self._canal

    def aumentar_vol(self):
        if self._volume == 100:
            print('Volume maximo!')
        else:
            self._volume += 1
            print(f'Volume: {self._volume}')

    def diminuir_vol(self):
        if self._volume == 0:
            print('Volume minimo!')
        else:
            self._volume -= 1
            print(f'Volume: {self._volume}')

    def mudar_canal(self, numero):
        if 1 > numero or numero > 60:
            print(f'Canal {numero} fora da Faixa Permitida')
        else:
            self._canal = numero
            print(f'Canal: {self._canal}')


if __name__ == '__main__':
    tv = TV()
    print(tv.volume)
    print(tv.canal)
    tv.aumentar_vol()
    tv.mudar_canal(13)
    tv.mudar_canal(70)
    print('-' * 20)
    # tv.volume = 200  # error!
    print(tv.volume)
    print(tv.canal)
