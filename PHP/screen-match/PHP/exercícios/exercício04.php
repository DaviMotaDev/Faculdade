<?php

//1.Escreva um programa em PHP que inicialize um array de notas e exiba somente as 3 maiores notas do array.

$notas = [8.5, 2.2, 7.3, 9.2, 6.1];
rsort($notas);

echo "As três maiores notas são: $notas[0], $notas[1], $notas[2]";

//2.Crie um programa em PHP que transforme a string “Vinicius Dias,1997,Programador” em um array em que cada item está separado por vírgulas.

$string = "Vinicius Dias,1997,Programador";

var_dump(explode(',', $string));

