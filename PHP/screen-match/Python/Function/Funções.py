print('Digite o primerio número')
valor1 = input()
print('Digite o segundo número')
valor2 = input()

def soma(v1, v2):
    v1 = int(v1)
    v2 = int(v2)
    soma = v1 + v2
    return soma

print(soma(valor1,valor2))