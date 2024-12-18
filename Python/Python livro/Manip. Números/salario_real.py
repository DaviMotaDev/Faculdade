salario = int(input('Digite seu salário: ')) # aqui declaramos que a variável digitada pelo usuário deve ser um número inteiro
imposto = float(input('Imposto em % (ex: 27.5): ')) # aqui declaramos que a variável digitada pelo usuário deve ser um número real "0.0"
print("valor real:{}".format(salario - (salario * (imposto * 0.01))))