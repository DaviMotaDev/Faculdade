<?php 

echo "Bem-vindo ao screen match! \n";

$nomeFilme = 'Top Gun - Maverick';
$nomeFilme = 'Thor: Ragnarok';
$nomeFilme = 'Watchmen';
$anoDeLancamento = $argv[1] ?? 2022;

$somaDeNotas = 9;
$somaDeNotas += 6;
$somaDeNotas += 8.5;
$somaDeNotas += 4;
$somaDeNotas += 7;

$notaFilme = $somaDeNotas / 5;
$planoPrime = true;

$incluidoNoPlano = $planoPrime || $anoDeLancamento < 2020;

echo 'Nome do filme: ' . $nomeFilme . "\n" . 'Nota Filme: ' . $notaFilme . "\n" . 'Ano de lançamento: ' . $anoDeLancamento ."/n";

if ($anoDeLancamento >= 2022){ 
    echo "esse filme é um lançamento";
} elseif ($anoDeLancamento > 2020 && $anoDeLancamento <= 2022) {
    echo "esse filme ainda é novo";
} else {
    echo "esse filme não é um lançamento";
}