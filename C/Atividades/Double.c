#include <stdio.h>

int main() {

    double A, B, C;
    double delta, x1, x2;

    printf("digite o pimeiro coeficente:");
    scanf("%lf", &A);

    printf("digite o segundo coeficente:");
    scanf("%lf", &B);

    printf("digite o terceiro coeficente:");
    scanf("%lf", &C);

    delta = B * B - 4 * A * C;
    x1 = (-B + sqrt(delta)) / (2 * A);//sqrt:é uma abreviação para “square root” (raiz quadrada) em matemática.
    x2 = (-B - sqrt(delta)) / (2 * A);

    printf("Raiz 1 (x1): %.2lf\n", x1);
    printf("Raiz 2 (x2): %.2lf\n", x2);
    
    return 0;
}