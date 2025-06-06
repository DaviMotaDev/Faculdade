<?php
//1 - Escreva um programa em PHP que exiba seu nome na tela.
$nome = 'Davi Mota Oliveira dos Santos';

echo $nome . "\n";

//2 - Crie um programa em PHP que calcule a média de três notas e exiba o resultado.

$notas = 7 + 8 + 4 + 6 + 2;
$calculoMedia = $notas / 5; 

echo "O resultado da média é: $calculoMedia" . "\n";

//3 - Elabore um programa em PHP que receba um valor em metros e converta para centímetros.

$comprimento = 3;
$convesaoParaCentimetros = ($comprimento) * 100;

echo 'comprimento: '. $comprimento . ' * 100' . ' = ' . $convesaoParaCentimetros . 'cm' . "\n"; 

//4 - Desenvolva um programa em PHP que verifique se um ano é bissexto ou não.

$ano = 2022; 

if (($ano % 4 == 0 && $ano % 100 != 0) || ($ano % 400 == 0)) {
    echo "$ano é um ano bissexto. \n";
} else {
    echo "$ano não é  um ano bissexto. \n";
}

//5 - Escreva um programa em PHP que converta uma temperatura de Celsius para Fahrenheit.

$celcius = 32;
$convesaoParaFahrenheit = ($celcius * 9/5) + 32;

echo "A temperatura de " . $celcius . '° Celsius é equivalente a ' . $convesaoParaFahrenheit .' Fahrenheit';