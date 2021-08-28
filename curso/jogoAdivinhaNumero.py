# Jogo Adivinha o Número

# Boas Vindas
# Sistema sorteia um número entre 1 e 100
# Sistema solicita o nome do jogador
# Sistema solicita ao jogador seu palpite
# Sistema compara o palpite do jogador com o número sorteado
# Se errou, informar se para mais ou para menos,
# solicitar outro palpite e informar quantas tentativas ainda restam
# Se acertou, parabenizar e informar o número de tentativas utilizadas.
# Número máximo de tentativas = 7

import random

print("##############################################")
print("Seja bem vindo(a) ao Jogo Advinha o Número")
print("##############################################")

print("Será sorteado um número entre 1 e 100.")
print("Você começará com um número máximo de 7 tentativas.")
numero_tentativas = 7
numero_sorteado = random.randrange(1, 101)
nome = input("Favor informar seu nome: ")
numero_palpite = 0

while numero_sorteado != numero_palpite and numero_tentativas >= 1:
    print(numero_sorteado)
    numero_palpite = int(input("Favor digitar seu palpite: "))
    if numero_sorteado < numero_palpite:
        numero_tentativas -= 1
        print("%s você errou, o número sorteado é menor que seu palpite!" % nome)
        if numero_tentativas == 0:
            print("Suas tentativas acabaram.")
        else:
            print("Ainda lhe resta %d tentativa(s)." % numero_tentativas)
    elif numero_sorteado > numero_palpite:
        numero_tentativas -= 1
        print("%s você errou, o número sorteado é maior que seu palpite!" % nome)
        if numero_tentativas == 0:
            print("Suas tentativas acabaram.")
        else:
            print("Ainda lhe resta %d tentativa(s)." % numero_tentativas)
    else:
        numero_tentativas_utilizadas = 8 - numero_tentativas
        print("PARABÉNS!!! %s você acertou!!! Foram utilizadas %d tentativa(s)." % (nome, numero_tentativas_utilizadas))
