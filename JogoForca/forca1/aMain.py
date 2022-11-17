from forca1 import principal1
from forca2 import principal2
# from forca1 import principal1


def menu():
    print(f'\033[1;35m=' * 12, 'BEM VINDO(A) AO JOGO DA FORCA', '=' * 12, '\033[0;0m')
    opcao = int(input('''\033[1;97m[1] - JOGO DA FORCA
[2] - ADICIONAR TEMA 
[3] - ESCREVER A PALAVRA\n\033[0;0m'''))
    if opcao == 1:
        principal1()
        opcao = int(input('''\033[1;97m[1] - NOVAMENTE
[2] - RETORNAR AO MENU
[3] - ENCERRAR\n\033[0;0m'''))
        if opcao == 1:
            return principal1()
        if opcao == 2:
            print('\n')
            return menu()

    elif opcao == 2:
        principal2()
        opcao = int(input('''\033[1;97m[1] - NOVAMENTE
[2] - RETORNAR AO MENU
[3] - ENCERRAR\n\033[0;0m'''))
        if opcao == 1:
            return principal2()
        if opcao == 2:
            print('\n')
            return menu()

    elif opcao == 3:
        pass


if __name__ == '__main__':
    menu()