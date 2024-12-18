imposto = 0.27   # aqui declaramos as variáveis
salario = 5000
salario2 = 3000

print("Salário real:{}".format(salario - (salario * imposto))) # aqui imprimimos o valor do salário real
# e utilizando "{}" e .format + a base para o calculo ser realizado entre ()
print("Imposto: {}".format(salario * imposto)) 

print("\nValor real: {0}".format(salario2 - (salario2 * imposto)))