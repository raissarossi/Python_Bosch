import random
def chute3():
    chute33 = int(input("3° chute: "))

def chute2():
    chute22 = int(input("2° chute: "))

def jogo():
    num = random.randint(1, 3)
    chute1 = int(input("1° chute: "))

    while True:

        if chute1 == num:
            print("ACERTOU:)")
            break

        if chute1 > num:
            print("O NUMERO SORTEADO É MENOR")
            return chute2()

        if chute1 < num:
            print("O NUMERO SORTEADO É MAIOR")
            return chute2()

        if chute22 == num:
            print("ACERTOU:)")
            break

        if chute22 > num:
            print("O NUMERO SORTEADO É MENOR")
            return chute3()

        if chute22 < num:
            print("O NUMERO SORTEADO É MAIOR")
            return chute3()



if __name__ == '__main__':
    jogo()

