import random 

def adv_coringa():
    coringa = 37
    tentativas_maximas = 5

    print("Bem vindo!")
    print("Tente adivinhar o número de 0 a 100")
    print("Você tem apenas 5 tentativas")

    while tentativas_maximas > 0:
        tentativa = int(input("Digite seu palpite: "))

        if tentativa == coringa:
            print("Parabéns você acertou!")
            return
        elif tentativa < coringa:
            print("Tente Novamente, o número coringa é maior!")
        else:
            print("Tente Novamente, o número coringa é menor!")

        tentativas_maximas -= 1
        if tentativas_maximas > 0:
            print(f"Você tem {tentativas_maximas} tentativas restantes!")

    print("Você perdeu, o número correto era:", coringa)

adv_coringa()
