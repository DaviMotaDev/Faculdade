# Classe PAI
class Veiculo:
    def __init__(self, qtde_rodas):
        self._qtde_rodas = qtde_rodas       # Aqui estamos utilizando o encapsulamento PROTEGIDO "_" _qtde_rodas

    def ligarMotor(self):
        print("O motor do veículo foi ligado")