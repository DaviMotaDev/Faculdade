from carro import Carro   #Do(from) arquivo carro.py, importar(import) a classe Carro.

meu_carro = Carro("Toyota", "Corolla", 2024, "Branca")
meu_segundo_carro = Carro("Fiat", "Palio", 2010, "Preto")

print("marca: "  + meu_carro.getMaraca())       #Aqui chamamos o atributo privado, através da classe criada em carro.py
print("modelo: "  + meu_carro.modelo)
print("ano: "  + str(meu_carro.ano))
print("cor: "  + meu_carro.cor)
print("quantidade de rodas: "  + str(meu_carro._qtde_rodas))         #por ser número inteiro é necessário concatenar para chamar o atributo

meu_carro.buzinar()
meu_segundo_carro.buzinar()
meu_carro.ligarMotor()