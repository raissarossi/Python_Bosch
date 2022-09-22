import random


f = ["banana", "maçã", "morango", "kiwi", "laranja"]
o = ["teclado", "garrafa", "armario", "tenis", "oculos"]
letrasE = ''
letrasC = ''
palpite = ''
todos = [f, o]
lista = random.choice(todos)
palavraSorteada = random.choice(lista)
print(palavraSorteada)
vazio = "_" * len(palavraSorteada)
forcaIMG = [f'''\033[1;97m

  +---+
  |   |
      |
      |
      |
      |
========\033[0;0m''', '''\033[1;97m

  +---+
  |   |
  O   |
      |
      |
      |
========\033[0;0m''', '''\033[1;97m

  +---+
  |   |
  O   |
  |   |
      |
      |
========\033[0;0m''', '''\033[1;97m

  +---+
  |   |
  O   |
 /|   |
      |
      |
========\033[0;0m''', '''\033[1;97m

  +---+
  |   |
  O   |
 /|\  |
      |
      |
========\033[0;0m''', '''\033[1;97m

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========\033[0;0m''', '''\033[1;97m

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========\033[0;0m''']

def intro():
    print(f'\033[1;35m='*12, 'BEM VINDO(A) AO JOGO DE FORCA', '='*12, '\033[0;0m')

    if lista == f:
        print(f'\033[1;31m\t\t\t\t\t\t\t\t\t\t\tDICA: Fruta\033[0;0m')

    if lista == o:
        print(f'\033[1;31m\t\t\t\t\t\t\t\t\t\t\tDICA: Objeto\033[0;0m')

    print(vazio)


def receberPalpite():
    palpite = input("Adivinhe uma letra: ").upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasC or palpite in letrasE:
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
def desenho():
    # global letrasC
    # global letrasE
    # global vazio
    print(forcaIMG[len(letrasE)])

    if palpite in palavraSorteada:
        letrasC += palpite
    else:
        letrasE += palpite

    for letra in letrasC:
        for x in range(len(palavraSorteada)):
            if letra == palavraSorteada[x]:
                vazio = vazio[:x] + letra + vazio[x + 1:]

    print('Acertos: ', letrasC)
    print('Erros: ', letrasE)
    print(vazio)
def perdeuJogo():
    if len(letrasE) == len(forcaIMG):
        return True
    else:
        return False
def ganhouJogo():
    ganhou = True
    for letra in palavraSorteada:
        if letra not in letrasC:
            ganhou = False
    return ganhou
def principal():
    print(intro())
    while True:
        palpite = receberPalpite()
        desenho(palavraSorteada, palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
        if ganhouJogo():
            print('Voce Ganhou!!!')


if __name__ == '__main__':
    principal()

