#include <stdio.h>

int main() {
    char char1, char2, char3;

    printf ("Digite o primeiro caracter: ");
    scanf (" %c", &char1);

    printf ("Digite o segundo caracter: ");
    scanf (" %c", &char2);

    printf ("Digite o terceir caracter: ");
    scanf (" %c", &char3);

    printf("Palavra formada: %c-%c-%c\n", char3, char2, char1);

    return 0;
}