#include <stdio.h>

int main() {

    int num1, num2;

    int subtracao;

    printf ("Digite o primeiro numero:");
    scanf ("%d", &num1);

    printf ("Digite o segundo numero:");
    scanf ("%d", &num2);

    subtracao = num1 - num2; 

    printf("Resultado da subtracao: %d", subtracao);

    return 0;
}