# JokenPyro

## O que é?

Um jogo de Jokenpô cliente-servidor desenvolvido em Python
que utiliza tecnologias RMI (Pyro).

Este projeto foi desenvolvido como parte da disciplina de Programação Distribuída (2016.2) da UFRN.

## Pré-Requisitos

Para executar o programa é preciso ter o Python3 instalado e a biblioteca [Pyro4](https://github.com/irmen/Pyro4).

## Execução

Primeiro, inicialize o servidor de nomes do Pyro4. Para isto utilize o script:

        $ ./startns.sh

Em seguida, execute o servidor do JokenPyro:

        $ python jokenpyro_server.py

Por fim, instancie um ou mais clientes para jogar:

        $ python jokenpyro.py
