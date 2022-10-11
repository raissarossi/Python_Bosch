#ADICIONAR TEMA
import os

def principal2():
    menu = int(input('''\033[1;97m[1] - ADICIONAR TEMA
[2] - ADICIONAR PALAVRA EM UM TEMA\n\033[0;0m'''))

    if menu == 1:
        while True:
            texto = input(f'\033[1;35mDIGITE O TEMA QUE DESEJA INCLUIR NO JOGO\n\033[0;0m').lower()
            texto += ".txt"
            arq = open(texto, "a+", encoding="utf-8")
            print(f'\033[1;36mAGORA INSIRA 3 PALAVRAS RELACIONADAS (sem acentuação)\033[0;0m')
            for x in range(0,3):
                palavraNovas = input(f'\033[1;97mPalavra {x+1}: ').lower()
                arq.write(palavraNovas+",")
                print(f'\033[1;32mADICIONADAS COM SUCESSO\n\033[0;0m')
            break
        arq.close()

    if menu == 2:
        while True:
            pasta = './'
            temas = []
            for diretorio, subpastas, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    if arquivo.__contains__(".txt"):
                        temas.append(str(os.path.join(diretorio, arquivo)).replace(".txt", "").replace("./", ""))
            temas = str(temas)
            temas = temas.replace("'", "").replace(',', ' --').replace('[', '').replace(']', '')
            print(temas)
            texto = input(f'\033[1;35mESCOLHA O TEMA QUE DESEJA INCLUIR PALAVRAS: \033[0;0m').lower()
            arq = open(texto+".txt", "a+", encoding="utf-8")
            qntd = int(input(f'\033[1;35mQUANTAS PALAVRAS DESEJA INCLUIR NO TEMA?\033[0;0m '))
            print(f'\033[1;36mAGORA INSIRA AS PALAVRAS RELACIONADAS (sem acentuação)\033[0;0m')
            for i in range(qntd):
                palavraNova = input(f'\033[1;97mPalavra em {texto}: ').lower()
                textoN = palavraNova + ","
                if p:
                    pass
                else:
                    arq.write(textoN)
                print(f'\033[1;32mADICIONADA COM SUCESSO\n\033[0;0m')
            break
        arq.close()



if __name__ == '__main__':
    principal2()



