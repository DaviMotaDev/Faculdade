programa {
  funcao inicio() {
  
    inteiro dia, mes, ano, idade, diaAtual, mesAtual, anoAtual

    escreva("Verifique a idade do cliente, através da identidade. \n") 
    
    escreva("Digite o dia de nascimento do cliente: ")
    leia(dia)

    escreva("Digite o mês de nascimento do cliente: ")
    leia(mes)

    escreva("Digite o ano de nascimento do cliente: ")
    leia(ano)
    
    diaAtual = 3
    mesAtual = 11
    anoAtual = 2024

    idade = anoAtual - ano 

    se(mesAtual < mes) 
    
    se(mesAtual == mes e diaAtual < dia) {
      idade = idade - 1
    }
    
    se(idade >= 18)
    {
      escreva("Está autorizado a comprar bebida alcoólica")
    }

    senao
    {
      escreva("O cliente ainda é menor de idade")
    } 
  }
}
