#include <stdio.h>

int main () {

    //declarações 

    int valInt1, valInt2, valIntRes;
    float valFloat, valFloatRes;

    //instruções
    
    //inicializa as variáveis interiaras

    valInt1 = 5;
    valInt2 = 10;

    //inicializa as variáveis reais
    valFloat= 2.7;

    valInt1 + valInt2; // soma valInt1 com valInt2 mas não amrazena em lugar nenhum -> comando "inutil"
    //pois não possui o comando valIntRes 

    valIntRes = valInt1 + valInt2; // soma valInt1 com valInt2 armazenando o resultado em valIntRes,
    //valIntRes possui valor 15

    valFloatRes = valFloat / 1.5; // valFloatRes possui valor 1.8

    valIntRes++; //igual a valIntRes = ValIntRes + 1; ou seja, valIntRes tinha valor 15 agora possui
    //valor 16

    printf("Valor de valIntRes: %d \n", valIntRes);
    printf("Valor de valFloatRes: %.2f", valFloatRes);

    return 0;
}