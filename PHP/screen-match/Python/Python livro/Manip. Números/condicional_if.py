salario = int(input('Valor do seu salário: ')) # aqui solicitamos que o usuário insira o seu salário.
imposto = input("Imposto em % (ex: 27.5): ") # aqui solicitamos que o usuário isira o imposto caso ele saiba.

if imposto == '':  # aqui iniciamos a condicional, no caso do usuário não informar o imposto ->
    imposto = 27.5 # irá adicionar automaticamente 27.5 de imposto.
    print("Imposto automático aplicado: 27.5")

else:      # se não o imposto será o que o usuário digitou.
    imposto = float(imposto)

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

print('{:_^60}'.format("Fim do código")) # sempre utilizar ":" no inicio das chaves

