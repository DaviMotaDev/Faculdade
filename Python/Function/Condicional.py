idade = int(input('Qual a sua idade? ')) 
#bloco de código para o usuário informar a idade
if idade >= 18:
    #bloco de código em caso de True
    print('É maior de idade')
else:
    #bloco de código em caso de False
    print('É menor de idade')

nota = float(input('Nota do aluno: '))

if nota >= 6.5:

    print('Aprovado')

else:

    print('Reprovado')

avaliação_nota = float(input('Qual foi a sua nota? '))
#Aqui utilizamos Float para variavél do tipo REAL e INPUT para pegar os dados do promt 
if avaliação_nota > 8:
#Se a nota for maior que 8 retornará -->
    print('Excelente nota!!')

elif avaliação_nota <= 8 and avaliação_nota >= 6:
#Se a nota for menor ou igual a 8 e estiver maior ou igual a 6 retornará
    print('está na média, pode melhorar em!')

else: 

    print('Você foi reprovado!')