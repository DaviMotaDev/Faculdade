from motor import Motor

class Carro:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor()
    def ligar_carro(self):
        print(f'ligando o carro da marca {self.marca}')
        self.motor.ligar()

    def deligar_carro(self):
        print(f'Desligando o carro da marca {self.marca}')