<?php

$saldo = 1000;
$titularDaConta = 'Davi Mota';

do {
    echo "1. Consultar saldo\n";
    echo "2. Realizar depósito\n";
    echo "3. Realizar saque\n";
    echo "4. Sair\n";

    $opcao = (int) fgets(STDIN);

    switch ($opcao) {
        case 1:
            echo "**************\n";
            echo "Titular: $titularDaConta\n";
            echo "Saldo atual: R$ $saldo\n";
            echo "**************\n";
            break;
        case 2:
            echo "digite o valor a ser depositado:";
            $valorDeposito = (float) fgets(STDIN);
            if ($valorDeposito <= 1) {
                echo "Não é possível depositar valor igual a 0 ou negavitivo\n";
            } else {
                $saldo += $valorDeposito;
            }
            break;
        case 3:
            echo "Qual valor deseja sacar?";
            $valorSaque = (float) fgets(STDIN);
            if ($valorSaque > $saldo) {
                echo "Você não possui saldo suficente para realizar a operação.\n";
            } else {
                $saldo -= $valorSaque;
            }
            break;
        case 4:
            echo "Adeus\n";
            break;
        default;
            echo "Opção inválida\n";
            break;
    }
} while ($opcao != 4);