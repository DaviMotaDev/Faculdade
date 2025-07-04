from veiculo import Veiculo     # Do(from) arquivo veículo, importar(import) a classe Veiculo.

class Carro(Veiculo):           # Aqui indicamos que Carro herdará atributos da classe Veiculo.

    def __init__(self, marca, modelo, ano, cor):
        self.__marca = marca        # Aqui estamos utilizando o encapsulamento PRIVADO "__"
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        super().__init__(4)     # Aqui puxamos o método da classe pai Veiculo

    def getMaraca(self):        # Aqui estamos criando uma função(def) para chamar o atributo __marca que será chamado no arquivo instancia_carro
        return self.__marca

    def buzinar(self):
        print("O carro " +self.modelo+ " Fez beep bepp")