<?php

function exibeMensagemLancamento(int $ano): void
{
    if ($ano >= 2022) {
        echo "esse filme é um lançamento \n";
    } elseif ($ano > 2020 && $ano <= 2022) {
        echo "esse filme ainda é novo \n";
    } else {
        echo "esse filme não é um lançamento \n";
    }
}

function incluidoNoPlano(bool $planoPrime, int $anoDeLancamento): bool
{
    return $planoPrime || $anoDeLancamento < 2020;
}

function criaFilme(string $nome, int $anoDeLancamento, float $nota, string $genero): Filme
{
    $filme = new Filme();

    $filme->nome = $nome;
    $filme->anoDeLancamento = $anoDeLancamento;
    $filme->genero = $genero;
    $filme->nota = $nota;

    return $filme;
}
