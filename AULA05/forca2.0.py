import random


f = ["banana", "manga", "morango", "kiwi", "laranja"]
o = ["teclado", "garrafa", "armario", "tenis", "oculos"]
letrasE = []
letrasC = []
letrasT = []
todos = [f, o]
lista = random.choice(todos)
palavraSorteada = random.choice(lista)
print(palavraSorteada)
vazio = "_" * len(palavraSorteada)
#imagens
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

def intro():
    print(f'\033[1;35m='*12, 'BEM VINDO(A) AO JOGO DE FORCA', '='*12, '\033[0;0m')
    # escolha = int(input('[1] - Jogar'
    #                     '[2] - Inserir palavra na forca'))
    # if escolha == '1':
    print(forcaIMG[0])
    print(f'\033[1;97m',vazio,'\033[0;0m')
    if lista == f:
        print(f'\033[1;31mDICA: Fruta\033[0;0m')
    if lista == o:
        print(f'\033[1;31mDICA: Objeto\033[0;0m')


def verificarLetra():
	fim = 0
	while True:
		if fim == 1:
			break
		while True:
			palpite = input("Chute uma letra: ").lower()
			if len(palpite) != 1:
				print('Coloque um unica letra.')
			elif palpite in letrasT:
				print('Voce ja disse esta letra.')
			elif not "a" <= palpite <= "z":
				print('Por favor escolha apenas letras')
			else:
				break

		temaletra = False
		for i in palavraSorteada:
			if i == palpite:
				temaletra = True
		if temaletra:
			letrasT.append(palpite)
			letrasC.append(palpite)

		else:
			letrasT.append(palpite)
			letrasE.append(palpite)

		verificador = 0
		if len(palavraSorteada) == verificador:
			print("\nGANHOU")
			break

		print(forcaIMG[len(letrasE)])

		if len(letrasE) >= 6:
			print(f'\nPERDEU:) a palavra é {palavraSorteada}')
			break


		for i in palavraSorteada:
			hide = True
			for j in letrasT:
				if i.lower() == j.lower():
					print(f'\033[1;97m',i,end="")
					verificador += 1
					hide = False
			if hide:
				print('-', end="")

		letras = str(letrasT)
		letras = letras.replace('[', '')
		letras = letras.replace(']', '')
		letras = letras.replace("'", '')

		print("\nLETRAS DIGITADAS: ", letras)
		print(f'\033[1;35m-_'*20,'\n\033[0;0m')
	jogarNovamente()




def jogarNovamente():
	novoJogo = input("CASO QUEIRA JOGAR NOVAMENTE INSIRA [S]").lower()
	if novoJogo == 's':
		print('\n')
		return principal()
	else:
		print('até mais')


def principal():
	intro()
	verificarLetra()


if __name__ == '__main__':

    principal()


