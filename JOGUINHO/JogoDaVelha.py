def vencedor(velha):
    l1 = velha[0]
    l2 = velha[1]
    l3 = velha[2]
    c1 = [velha[0][0], velha[1][0], velha[2][0]]
    c2 = [velha[0][1], velha[1][1], velha[2][1]]
    c3 = [velha[0][2], velha[1][2], velha[2][2]]
    d1 = [velha[0][0], velha[1][1], velha[2][2]]
    d2 = [velha[0][2], velha[1][1], velha[2][0]]
    tudo = [l1,l2,l3,c1,c2,c3,d1,d2]
    resto = 0

    for x in range(0, len(tudo)):
        # print(tudo[x])
        if tudo[x] == ['X', 'X', 'X']:
            print('JOGADOR 1 GANHOU')
            return False

        elif tudo[x] == ['O', 'O', 'O']:
            print('JOGADOR 2 GANHOU')
            return False

        for y in range(0,3):
            # print(t3udo[x][y])
            if tudo[x][y] != 'X':
                if tudo[x][y] != 'O':
                    resto = 1
    print(resto)
    if resto == 0:
        print("iiiiiiii deu velha hahaha muito ruim voces")
        return False
    return True

def jogador(velha, xo):
    marcador = xo
    while True:
        marcar = int(input("DIGITE ONDE DESEJA MARCAR\n"))
        x, y = verificar(marcar)
        if x == 10:
            print("DIGITE UMA POSIÇÃO VÁLIDA")
            convert(velha)
        elif not velha[x][y] == "X" and not velha[x][y] == "O":
            velha[x][y] = marcador
            break
        else:
            print("JA ESTA MARCADO")
            convert(velha)

    # pass
def verificar(marcar):

    if marcar == 7:
        x = 0
        y = 0
    elif marcar == 8:
        x = 0
        y = 1
    elif marcar == 9:
        x = 0
        y = 2
    elif marcar == 4:
        x = 1
        y = 0
    elif marcar == 5:
        x = 1
        y = 1
    elif marcar == 6:
        x = 1
        y = 2
    elif marcar == 1:
        x = 2
        y = 0
    elif marcar == 2:
        x = 2
        y = 1
    elif marcar == 3:
        x = 2
        y = 2
    else:
        x = 10
        y = 10

    return x, y
def convert(velha):
    jogo = str(velha)
    jogo = jogo.replace('[[', '')
    jogo = jogo.replace('[', '\n')
    jogo = jogo.replace(']', '')
    jogo = jogo.replace(',', '')
    jogo = jogo.replace('0', '')
    jogo = jogo.replace("'", '')

    print(jogo)


if __name__ == '__main__':
    velhaL1 = [[70, 80, 90],
               [40, 50, 60],
               [10, 20, 30]]
    # print(velhaL1[0])
    # velhaL1[0][0] = 1
    # print(velhaL1[0])
    convert(velhaL1)
    while True:
        jogador(velhaL1, "X")
        continuar = vencedor(velhaL1)
        convert(velhaL1)
        if not continuar:
            break

        jogador(velhaL1, "O")
        continuar = vencedor(velhaL1)
        convert(velhaL1)

        if not continuar:
            break
