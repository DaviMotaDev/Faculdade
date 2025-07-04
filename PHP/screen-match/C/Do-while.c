#include <stdio.h>

int main () {

    int num;
     
    num = -1;

    while (num != 0)
    {

        printf ("Digite um numero inteiro (0 para sair):");
        scanf ("%d", &num);
        printf("Numero digitado: %d\n", num);

    }
    
    return 0;
    
}