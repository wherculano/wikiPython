"""
Implemente uma classe chamada Carro com as seguintes propriedades:
Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina.
Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque.
Exemplo de uso:
meuFusca = Carro(15);
# 15 quilômetros por litro de combustível. meuFusca.adicionarGasolina(20);
# abastece com 20 litros de combustível. 
meuFusca.andar(100);
# anda 100 quilômetros.
meuFusca.obterGasolina()
# Imprime o combustível que resta no tanque.
"""


class Carro:
    def __init__(self, consumo, tanque=0):
        self.consumo = consumo
        self.qtd_comb = tanque

    def adicionarGasolina(self, litros):
        self.qtd_comb += litros
        print(f'Você abasteceu {litros} litros de gasolina.\n')

    def andar(self, km):
        if self.qtd_comb == 0:
            print('O carro não pode andar pois está sem gasolina.\n')
        elif (km / self.consumo) > self.qtd_comb:
            print(
                f'Nao será possível andar {km}km com apenas {self.qtd_comb} litros no tanque.\n'
                f'Para tal, você precisará abastecer no minimo mais'
                f'{(km - (self.qtd_comb * self.consumo)) / self.consumo:.2f} litros de gasolina.\n')
        else:
            self.qtd_comb -= (km / self.consumo)
            print(f'O carro andou {km}km.\n')

    def obterGasolina(self):
        print(f'Há {self.qtd_comb:.2f} litros de gasolina.\n')


if __name__ == '__main__':
    # 15 quilômetros por litro de combustível
    meuFusca = Carro(15)
    # Imprime o combustível que resta no tanque.
    meuFusca.obterGasolina()
    # anda 100 quilômetros.
    meuFusca.andar(100)
    # abastece com 20 litros de combustível.
    meuFusca.adicionarGasolina(20)

    meuFusca.andar(400)
    meuFusca.adicionarGasolina(10)
    meuFusca.obterGasolina()
    meuFusca.andar(400)
    meuFusca.obterGasolina()
