import random

def jogar():

    print('\n')
    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')
    print('\n')

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))
    print('\n')

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada  in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

        chute_str = input('Digite um número entre 1 a 100: ')
        print('Você digitou', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Você ACERTOU e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi MAIOR do que o número secreto.')
            elif(menor):
                print('Você errou! O seu chute foi MENOR do que o número secreto.')
            pontos_perdidos = abs(chute - numero_secreto)
            pontos = pontos - pontos_perdidos

if(__name__ == '__main__'):
    jogar()