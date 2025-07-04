from circulo import Circulo
from quadrado import Quadrado
from retangulo import Retangulo

meu_circulo = Circulo(2)
meu_retangulo = Retangulo(3, 2)
meu_quadrado = Quadrado(4)

print(str(meu_circulo.calcular_area()))
print(str(meu_retangulo.calcular_area()))
print(str(meu_quadrado.calcular_area()))