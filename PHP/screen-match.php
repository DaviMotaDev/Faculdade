<?php 

echo "Bem-vindo ao screen match! \n";

$nomeFilme = 'Top Gun - Maverick';
$nomeFilme = 'Se beber não case';
$nomeFilme = 'Thor: Ragnarok';

$anoDeLancamento = 2022;

$quantidadeDeNotas = $argc - 1;
$nota =[];

for ($contador = 1; $contador < $argc; $contador++) {
    $notas[] = (float) $argv[$contador];
}

$notaFilme = array_sum($notas) / $quantidadeDeNotas;
$planoPrime = true;

$incluidoNoPlano = $planoPrime || $anoDeLancamento < 2020;

echo 'Nome do filme: ' . $nomeFilme . "\n" . 'Nota Filme: ' . $notaFilme . "\n" . 'Ano de lançamento: ' . $anoDeLancamento ."\n";

if ($anoDeLancamento >= 2022){ 
    echo "esse filme é um lançamento \n";
} elseif ($anoDeLancamento > 2020 && $anoDeLancamento <= 2022) {
    echo "esse filme ainda é novo \n";
} else {
    echo "esse filme não é um lançamento \n";
}

$genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "ação",
    "Thor: Ragnarok" => "super-herói",
    "Se beber não case" => "comédia",
    default => "gênero desconhecido"
};

echo 'O gênero do filme é:' . $genero;

var_dump($argv);
