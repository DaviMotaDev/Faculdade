#include <stdio.h>
 
 int main() {

    //declarações
    int i;

    i = 0;

    while (i < 5) //estrutura de repetição: inicio 0 fim 4
    {
        printf ("valor de i: %d\n", i);

        i = i + 5;

    }

    printf("Saiu o laco!\n");

    return 0;     
}