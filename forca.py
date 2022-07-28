from operator import index
import jogos
import sys

def jogar():
    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    print("*********************************")
    print("Bem vindo ao jogo da forca!")
    print("*********************************")
    print("*********************************")

    while(not enforcou and not acertou):
        chute = input("Qual e a letra?")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print("Encontrei a letra '{}' na posição '{}'".format(letra, index))
            index += 1
        
        print("Jogando....")


    print("*********************************")
    print("Fim do jogo")
    print("*********************************")
    continuar_jogando()

def continuar_jogando():

    continua = int(input("Deseja continuar jogando (1), Escolher outro jogo (2), Sair do Pick-Jogos (3): "))
   
    if continua == 1:
        jogar()
    elif continua == 2:
        jogos.pick_jogos() 
    else:
        print("*********************************")
        print("Fechando o Pick-Jogos")
        print("*********************************")
        sys.exit()
    
if __name__  == "__main__":
    jogar()