<?php

//1 - Escreva um programa que exiba, na tela do usuário, todos os números ímpares de 0 à 100.

for ($numero = 0; $numero <= 100; $numero++) {
    if ($numero % 2 != 0) {
        echo $numero . ",";
    }
}

//2 - Crie um programa que, a partir de altura e peso, calcule o IMC e exiba a classificação do IMC.

$peso = 72;
$altura = 1.75;

$calculoIMC = $peso / ($altura * 2);
$arredondando = round($calculoIMC, 2);

echo "\nO indice de massa corporal é: $arredondando \n";

/*3 - Desenvolva um programa que exiba na tela uma saudação (bom dia, boa tarde ou boa noite) 
dependendo do horário encontrado em uma variável (inteiro representando as horas).*/

$horarioDoDia = 10;

if ($horarioDoDia >= 0 && $horarioDoDia<= 12) {
    echo "São $horarioDoDia horas \nBom Dia!";
} elseif ($horarioDoDia >=  12 && $horarioDoDia <= 18) {
    echo "São $horarioDoDia horas \nBoa Tarde!";
} elseif ($horarioDoDia >= 18 && $horarioDoDia <= 23) {
    echo "São $horarioDoDia horas \nBoa Noite!";
} else {
    echo "Hora inválida!";
}
