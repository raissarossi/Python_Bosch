#ADICIONAR TEMA
def principal2():
    menu = int(input('''\033[1;97m[1] - ADICIONAR TEMA
[2] - ADICIONAR PALAVRA EM UM TEMA\n\033[0;0m'''))

    if menu == 1:
        cont = 0
        while True:
            texto = input(f'\033[1;35mDIGITE O TEMA QUE DESEJA INCLUIR NO JOGO\n\033[0;0m').lower()
            texto += ".txt"
            arq = open(texto, "a+", encoding = "utf-8")
            print(f'\033[1;36mAGORA INSIRA 3 PALAVRAS RELACIONADAS (sem acentuação)\033[0;0m')
            for x in range(0,3):
                palavraNovas = input(f'\033[1;97mPalavra {x+1}: ').lower()
                arq.write(palavraNovas+",")
                print(f'\033[1;32mADICIONADAS COM SUCESSO\n\033[0;0m')
            break
        arq.close()

    if menu == 2:
        texto = input(f'\033[1;35mDIGITE O TEMA QUE DESEJA INCLUIR NO JOGO: \033[0;0m').lower()
        arq = open(texto+".txt", "a+", encoding="utf-8")
        print(f'\033[1;36mAGORA INSIRA A PALAVRA RELACIONADA (sem acentuação)\033[0;0m')
        palavraNova = input(f'\033[1;97mPalavra em {texto}: ').lower()
        texto = palavraNova + ","
        arq.write(texto)
        print(f'\033[1;32mADICIONADA COM SUCESSO\n\033[0;0m')
        # print(palavraNova)
        arq.close()


if __name__ == '__main__':
    principal2()



