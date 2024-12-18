salario = int(input('Valor do seu salário: ')) # aqui solicitamos que o usuário insira o seu salário.
imposto = float(input("Imposto: ")) # aqui solicitamos que o usuário isira o imposto caso ele saiba.

if imposto < 10:  
    print("Médio") 

elif imposto < 27.5: # aqui utiizamos o elif para garanti que se o imposto passar de 27.5% o usuário será alertado.
    print("Alto")

else: 
    print("Muito alto")

print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))

print('{:_^60}'.format("Fim do código")) # sempre utilizar ":" no inicio das chaves

