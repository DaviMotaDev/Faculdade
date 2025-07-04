#include <stdio.h>

int main () { 

    float dist, temp, velocidade;

    printf ("Digite a distancia:");

    scanf ("%f", &dist);

    printf ("Digite o tempo:");

    scanf ("%f", &temp);

    velocidade = dist / temp;

    printf ("Velocidade: %.2f", velocidade);

    return 0;

}