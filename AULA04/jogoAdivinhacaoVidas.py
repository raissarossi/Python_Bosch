import random

def jogo():
    num = random.randint(1, 101)
    vida = 50
    chances = 1
    print(f'\033[1;35m='*12, 'CHUTE UM NÚMERO ENTRE 1 E 100', '='*12, '\033[0;0m')
    print(f'\033[1;31m\t\t\t\t\t\t\t\t\t\t\t♥ VIDA:{vida}\033[0;0m')

    while chances <= 3:
        texto = "CHANCE " + str(chances) + ": "
        while True:
            try:
                chute = int(input(f'\033[1;97m{texto}\033[0;0m'))
                break
            except:
                print(f'\033[1;36mVOCÊ NÃO DIGITOU UM NÚMERO\033[0;0m')
                print(f'\033[1;35mPARA FICAR ESPERTO VOCÊ PERDEU 10 VIDAS\033[0;0m')
                vida = vida-10
                print(f'\033[1;35m-\033[0;0m' * 55)
                print(f'\033[1;31m\t\t\t\t\t\t\t\t\t\t\t♥ VIDA:{vida}\033[0;0m')
                if vida <= 0:
                    chute = num
                    break
        if vida <= 0:
            print(f'\033[1;31mPERDEU:(\033[0;0m')
            print(f'''\033[1;95mSUAS VIDAS ACABARAM
O NÚMERO SORTEADO É: {num}\033[0;0m''')
            break

        if chute == num:
            print(f'\033[1;32mACERTOU:)\033[0;0m')
            break

        if chute > num:
            vd = chute - num
            vida = vida - vd
            if vida <= 0:
                print(f'\033[1;31mPERDEU:(\033[0;0m')
                print(f'''\033[1;95mSUAS VIDAS ACABARAM
O NÚMERO SORTEADO É: {num}\033[0;0m''')
                break
            else:
                print(f'\033[1;36mO NUMERO SORTEADO É MENOR\033[0;0m')
                print(f'\033[1;35m-\033[0;0m' * 55)
                print(f'\033[1;31m\t\t\t\t\t\t\t\t\t\t\t♥ VIDA:{vida}\033[0;0m')


        if chute < num:
            vd = num - chute
            vida = vida - vd
            if vida <= 0:
                print(f'\033[1;31mPERDEU:(\033[0;0m')
                print(f'''\033[1;95mSUAS VIDAS ACABARAM
O NÚMERO SORTEADO É: {num}\033[0;0m''')
                break
            else:
                print(f'\033[1;36mO NUMERO SORTEADO É MAIOR\033[0;0m')
                print(f'\033[1;35m-\033[0;0m' * 55)
                print(f'\033[1;31m\t\t\t\t\t\t\t\t\t\t\t♥ VIDA:{vida}\033[0;0m')


        if chances == 3:
            print(f'''\033[1;95mSUAS CHANCES ACABARAM
O NÚMERO SORTEADO É: {num}\033[0;0m''')

        chances = chances + 1


if __name__ == '__main__':
    jogo()


