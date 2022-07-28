import forca
import adivinacao
import sys

def pick_jogos():

    print("*********************************")
    print("*********************************")
    print("***********Bem-Vindo*************")
    print("!!!!!!!!!!Pick-Jogos!!!!!!!!!!!!!")
    print("*********************************")
    print("*********************************")

    print("(1) Forca (2) Advinhação (3) Fechar o Pick-Jogos")

    jogo= int(input("Escolha um jogo: "))

    if jogo == 1:
        print("Abrindo jogo de Forca")
        forca.jogar()
        if jogo == 2:
            print("Abrindo jogo de Advinhação")
            adivinacao.jogar()
    else:
        print("*********************************")
        print("Fechando o Pick-Jogos")
        print("*********************************")
        sys.exit()


if __name__  == "__main__":
    pick_jogos()