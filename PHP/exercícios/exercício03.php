<?php

/*1 - Escreva um programa em PHP que remova os elementos duplicados de um array fornecido
 como entrada e exiba o array resultante. Por exemplo, se o array for [1, 2, 2, 3, 4, 4, 5],
  o programa deve exibir [1, 2, 3, 4, 5].*/

$array = [1, 2, 2, 3, 4, 4, 5];
$semDuplicatas = array_unique($array);

/*2 - Percorra um array de notas (cada uma de 0 a 10) e exiba a nota do aluno em questão
 com a informação se o aluno foi aprovado ou não.*/

$notas = [10, 5.5, 3.8, 7.5, 6, 6.1, 5.9];

foreach ($notas as $nota) {
    $resultado = $nota > 6 ? "aprovado" : "reprovado";

    echo "Esse(a) aluno(a) foi $resultado com a nota $nota \n";
}

