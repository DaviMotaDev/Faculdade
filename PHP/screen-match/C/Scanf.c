#include <stdio.h>

int main () {

    int idade;
    float valorDoPgto;
    double velParticula;
    char tipoHabMotor;

    printf("Informe a idade:");
    scanf("%d", &idade);
    printf("Informe valor do pagamento:");
    scanf("%f", &valorDoPgto);
    printf("Informe a velocidade da particula:");
    scanf("%lf", &velParticula);
    printf("informe o tipo de habilitacao:");
    scanf(" %c", &tipoHabMotor);

    printf("Dados informados: %d, %f, %lf, %c\n", idade,valorDoPgto, velParticula, tipoHabMotor);
 
    return 0; 
}