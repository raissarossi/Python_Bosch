#JOGO DA FORCA DIRETO
import random
import os

def principal1():
    pasta = './'
    temas = []
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.__contains__(".txt"):
                temas.append(str(os.path.join(diretorio, arquivo)).replace("./", ""))
    # print(temas)
    # f = ["banana", "manga", "morango", "kiwi", "laranja"]
    # o = ["teclado", "garrafa", "armario", "tenis", "oculos"]
    # todos = [f, o]
    tema = random.choice(temas)
    arq = open(tema,"r", encoding="utf-8")
    txtarq = arq.read()
    palavra = ''
    lista = []
    for i in txtarq:
        if i != ",":
            palavra += i
        else:
            lista.append(palavra)
            palavra = ''
    palavraSorteada = random.choice(lista)
    print(palavraSorteada)
    arq.close()
    tema = tema.replace(".txt", "")
    vazio = "_" * len(palavraSorteada)
    # imagens
    forcaIMG = [f'''\033[1;36m
		  +---+
		  |   |
		      |
		      |
		      |
		      |
		========\033[0;0m''', '''\033[1;36m
		  +---+
		  |   |
		 \033[1;31m O   \033[1;36m|
		      |
		      |
		      |
		========\033[0;0m''', '''\033[1;36m
		  +---+
		  |   |
		 \033[1;31m O   \033[1;36m|
		 \033[1;31m |   \033[1;36m|
		      |
		      |
		========\033[0;0m''', '''\033[1;36m
		  +---+
		  |   |
		 \033[1;31m O   \033[1;36m|
		 \033[1;31m/|   \033[1;36m|
		      |
		      |
		========\033[0;0m''', '''\033[1;36m
		  +---+
		  |   |
		 \033[1;31m O   \033[1;36m|
		 \033[1;31m/|\  \033[1;36m|
		      |
		      |
		========\033[0;0m''', '''\033[1;36m
		  +---+
		  |   |
		 \033[1;31m O   \033[1;36m|
		 \033[1;31m/|\  \033[1;36m|
		 \033[1;31m/    \033[1;36m|
		      |
		========\033[0;0m''', '''\033[1;36m
		  +---+
		  |   |
		 \033[1;31m O   \033[1;36m|
		 \033[1;31m/|\  \033[1;36m|
		 \033[1;31m/ \  \033[1;36m|
		      |
		========\033[0;0m''']
    intro(forcaIMG, vazio, tema)
    verificarLetra(forcaIMG, palavraSorteada)


def intro(forcaIMG, vazio, tema):
    print(f'\033[1;35m=' * 20, 'JOGO DA FORCA', '=' * 20, '\033[0;0m')
    print(forcaIMG[0])
    print(f'\033[1;97m', vazio, '\033[0;0m')
    print(f'\033[1;31mDICA: {tema}\033[0;0m')



def verificarLetra(forcaIMG, palavraSorteada):
    letrasE = []
    letrasC = []
    letrasT = []
    fim = 0
    while True:
        if fim == 1:
            break
        while True:
            palpite = input("Chute uma letra: ").upper()
            if len(palpite) != 1:
                print('Coloque um unica letra.')
            elif palpite in letrasT:
                print('Voce ja disse esta letra.')
            elif not "A" <= palpite <= "Z":
                print('Por favor escolha apenas letras')
            else:
                break

        temaletra = False
        for i in palavraSorteada:
            if i.upper() == palpite:
                temaletra = True

        if temaletra:
            letrasT.append(palpite)
            letrasC.append(palpite)

        else:
            letrasT.append(palpite)
            letrasE.append(palpite)

        verificador = 0

        print(forcaIMG[len(letrasE)])

        if len(letrasE) >= 6:
            print(f'\nPERDEU:) a palavra é {palavraSorteada}')
            break

        for i in palavraSorteada:
            hide = True
            for j in letrasT:
                if i.upper() == j.upper():
                    print(f'\033[1;97m', i.upper(), end="")
                    verificador += 1
                    hide = False
            if hide:
                print('-', end="")

        if len(palavraSorteada) == verificador:
            print("\nGANHOU")
            break

        letras = str(letrasT)
        letras = letras.replace('[', '')
        letras = letras.replace(']', '')
        letras = letras.replace("'", '')

        print("\nLETRAS DIGITADAS: ", letras)
        print(f'\033[1;35m-_' * 20, '\n\033[0;0m')


if __name__ == '__main__':
    principal1()