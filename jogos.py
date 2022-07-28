import forca
import adivinacao

def pick_jogos():

    print("*********************************")
    print("*********************************")
    print("***********Bem-Vindo*************")
    print("!!!!!!!!!!Pick-Jogos!!!!!!!!!!!!!")
    print("Escolha seu jogo")
    print("*********************************")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo= int(input("Escolha o jogo: "))

    if jogo == 1:
        print("Abrindo jogo de Forca")
        forca.jogar()
    elif jogo == 2:
        print("Abrindo jogo de Advinhação")
        adivinacao.jogar()


    print("*********************************")
    print("Fechando o Pick-Jogos")
    print("*********************************")

if __name__  == "__main__":
    pick_jogos()