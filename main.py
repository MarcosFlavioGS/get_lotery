#!/usr/bin/env python3

from megasena import mega_sena
from loto_facil import loto_facil

replay = '1'
while (replay == '1'):
    print("Bem vindo ao gerador de números da loteria!")
    print("Escolha uma das opções abaixo:")
    print("1 - Mega Sena")
    print("2 - Lotofácil")

    choice = int(input("Qual a sua escolha ? "))
    if choice == 1:
        print("Bem vindo ao gerador de números da Mega Sena!")
        mega_sena()
    elif choice == 2:
        print("Bem vindo ao gerador de números da Lotofácil!")
        loto_facil()
    replay = input("Deseja jogar novamente ? (1 - Sim / 2 - Não) ")

input("Finazizando programa, pressione qualquer tecla para sair...")
