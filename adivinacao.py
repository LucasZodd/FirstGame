import jogos
import random
import sys


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    print("*********************************")
    print("Qual e o nível de dificuldade?")
    print("Fácil (1), Médio (2) Difícil (3)")
    dificuldade = int(input("Seleciona o nível do jogo: "))
    print("*********************************")

    if dificuldade == 1:
        total_tentativas = 10
    elif dificuldade == 2:
        total_tentativas = 5
    else:
        total_tentativas = 3

    max_numero = 30
    numero_secreto = round(random.randrange(1, max_numero))
    tentativas = 1
    pontos = 1000

    print(numero_secreto)
    for rodada in range(1, total_tentativas + 1):
        chute = int(input("Adivinhe um número entre 1 a {} :" .format(max_numero)))
        print("=================================")
        print("Vocẽ chutou:", chute)

        acertou = chute == numero_secreto
        numero_maior = chute > numero_secreto
        tentativas_restantes = total_tentativas - tentativas

        if chute < 1 or chute > max_numero:
            print("Vocẽ deve digitar um número entre 1 a {}. Restam {} tentativas" .format(max_numero, tentativas_restantes))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            tentativas += 1
            continue

        if acertou:
            break        
        else:
            if tentativas == total_tentativas:
                break
            
            if numero_maior and tentativas_restantes > 1:
                print("Vocẽ errou, número maior do que o número secreto. Restam {} tentativas" .format(tentativas_restantes))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            if not numero_maior and tentativas_restantes > 1:
                print("Vocẽ errou, número menor que o número secreto. Restam {} tentativas" .format(tentativas_restantes))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            elif numero_maior and tentativas_restantes == 1:
                print("Vocẽ errou, número maior do que o número secreto. Resta {} tentativa" .format(tentativas_restantes))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            elif not numero_maior and tentativas_restantes == 1:
                print("Vocẽ errou, número menor que o número secreto. Resta {} tentativa" .format(tentativas_restantes))
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
    
        tentativas += 1

    if tentativas_restantes == 0 and chute != numero_secreto:  
        print("*********************************")
        print("Você gastou todas as suas tentativas")
        print("Número secreto era:", numero_secreto)
        print("Game Over!")
        print("*********************************")

        continuar_jogando()

    else:
        print("*********************************")
        print("Você ganhou!!!! número era:", numero_secreto)
        print("Sua pontuação total:", pontos)
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
        sys.exit()
    
if __name__  == "__main__":
    jogar()