<?php

require __DIR__."/src/model/filme.php";
require __DIR__."/src/funcoes.php";

echo "Bem-vindo ao screen match! \n";

$nomeFilme = 'Top Gun - Maverick';
$nomeFilme = 'Se beber não case';
$nomeFilme = 'Thor: Ragnarok';

$anoDeLancamento = 2022;

$quantidadeDeNotas = $argc - 1;
$nota = [];

for ($contador = 1; $contador < $argc; $contador++) {
    $notas[] = (float) $argv[$contador];
}

$notaFilme = array_sum($notas) / $quantidadeDeNotas;
$planoPrime = true;

$incluidoNoPlano = incluidoNoPlano($planoPrime, $anoDeLancamento);


echo 'Nome do filme: ' . $nomeFilme . "\n" . 'Nota Filme: ' . $notaFilme . "\n" . 'Ano de lançamento: ' . $anoDeLancamento . "\n";

exibeMensagemLancamento($anoDeLancamento);

$genero = match ($nomeFilme) {
    "Top Gun - Maverick" => "ação",
    "Thor: Ragnarok" => "super-herói",
    "Se beber não case" => "comédia",
    default => "gênero desconhecido"
};

echo 'O gênero do filme é:' . $genero;

$filme = criaFilme(
    nome:"Thor: Ragnarok",
    anoDeLancamento:"2021",
    nota:"7.8",
    genero:"super-herói");

echo $filme->anoDeLancamento;

var_dump($notas);
sort($notas);
var_dump($notas);
$menorNota = min($notas);
var_dump($menorNota);

var_dump($filme->nome);
$posicaoDoisPontos = strpos($filme->nome,':');
var_dump($posicaoDoisPontos);

var_dump(substr($filme->nome, 0, $posicaoDoisPontos));

$filmeComStringJson = json_encode($filme);
file_put_contents(__DIR__ . '/filme.json', $filmeComStringJson);
