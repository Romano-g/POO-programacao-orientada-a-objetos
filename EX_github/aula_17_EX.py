"""
Exercício com classes
1 - Crie uma classe Carro (nome) *
2 - Crie uma classe Motor (nome) *
3 - Crie uma classe Fabricante (nome) *
4 - Faça a ligação entre Carro tem Motor *
OBS = Um motor pode ser de vários carros *
5 - Faça a ligação entre Carro e Fabricante *
OBS = Um fabricante pode fabricar vários carros *
Exiba nome do carro, motor e fabricantes na tela *
"""


class Carro:
    def __init__(self, nome):
        self.carros = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def printa(self, carro):
        print(
            f'Motor - {carro.motor.modelo}, Fabricante - {carro.fabricante.marca}, Modelo - {carro.carros}')


class Motor:
    def __init__(self, nome):
        self.modelo = nome


class Fabricantes:
    def __init__(self, nome):
        self.marca = nome


MOTOR = Motor('V8')
MOTOR2 = Motor('V6')
MOTOR3 = Motor('1.0')

VOLKS = Fabricantes('Volkswagen')
FORD = Fabricantes('Ford')
MERCEDEZ = Fabricantes('Mercedez')

celta = Carro('Celta')
celta.fabricante = VOLKS
celta.motor = MOTOR

gol = Carro('Gol')
gol.fabricante = FORD
gol.motor = MOTOR2

uno = Carro('Uno')
uno.fabricante = MERCEDEZ
uno.motor = MOTOR3

celta.printa(celta)
gol.printa(gol)
uno.printa(uno)
