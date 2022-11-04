import inquirer
from creditos import Creditos
import sys

print(f'\033[1;36m='*10,'BEM VINDO(A) AO JOGO DOS DADOS','='*10,'\033[0;00m')
dinheiro = Creditos()
valorCredito = dinheiro.depositarCreditos()

#-*- coding: UTF-8

while True:
    iniciar =  [
        inquirer.List(
            'escolha',
            message= f'\033[1;36mINICIAR JOGO? \033[0;0m',
            choices= ('SIM', 'NÃO'))
        ]
    inicio = inquirer.prompt(iniciar)['escolha']

    if inicio == 'SIM':
        while(True):
            if dinheiro.valor < 2:
                print(f'\033[1;31mCRÉDITOS INSUFICIENTES: {dinheiro.valor}','='*26,'\033[0;0m')
                depositar = [
                        inquirer.List(
                            'escolha',
                            message= f'\033[1;36mDEPOSITAR MAIS CRÉDITOS?\033[0;00m',
                            choices = ('SIM', 'SAIR'))        
                        ]
                deposito = inquirer.prompt(depositar)['escolha']

                if deposito == 'SIM':
                    print(f'\033[1;33mVAMOS LÁ\033[0;0m')
                    valorCredito = dinheiro.depositarCreditos()
                    break
                elif deposito == 'SAIR':
                    break
                else:
                    pass


            dinheiro.valor -= 2
            qnt = 51- len(str(self.valor)) - 10
            print(f'\033[1;35mCRÉDITOS: {dinheiro.valor}','='*qnt,'\033[0;0m')
            dinheiro.jogoDados()

            jogarDnv = [
                        inquirer.List(
                            'escolha',
                            message= f'\033[1;36mJOGAR NOVAMENTE?\033[0;0m',
                            choices = ('SIM', 'NÃO'))        
                        ]
            jogarNovamente = inquirer.prompt(jogarDnv)['escolha']

            if jogarNovamente == 'SIM':
                print(f'\033[1;33mVAMOS LÁ\033[0;0m')
            elif jogarNovamente == 'NÃO':
                dinheiro.sacar()
                sys.exit()


    elif inicio == 'NÃO':
        qnt = 51- len(str(self.valor)) - 10
        print(f'\033[1;35mCRÉDITOS: {dinheiro.valor}','='*qnt,'\033[0;0m')
        dinheiro.sacar()
        break


