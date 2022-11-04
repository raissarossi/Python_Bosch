#-*- coding: UTF-8
import time
import inquirer
import random

class Creditos:
    
    def __init__(self):
        self.valor = 0

    def depositarCreditos(self):
        valorvalor = int(input(f'\033[1;35mINSIRA O VALOR DESEJADO:\n\033[0;0m'))
        # print(valorvalor)
        self.valor += valorvalor
        print('\033[1;32mSEUS CRÉDITOS FORAM ADICIONADOS','='*20,'\n\033[0;0m')
        qnt = 51- len(str(self.valor)) - 10
        print(f'\033[1;35mCRÉDITOS: {self.valor}','='*qnt,'\033[0;0m')
    
    def jogoDados(self):
        revanche = False
        while True:
            chuteUser = [
                inquirer.List(
                    'escolha',
                    message= f'\033[1;36mSEU CHUTE\033[0;00m',
                    choices = (1, 2, 3, 4, 5, 6))        
                ]
            chuteUsuario = inquirer.prompt(chuteUser)['escolha']
            print(f'\033[1;35mSUA APOSTA: {chuteUsuario}\033[0;0m')

            while True:
                chuteComputador = random.randint(1, 6)
                if chuteComputador == chuteUsuario:
                    continue
                elif chuteComputador != chuteUsuario:
                    break
            print(f'\033[1;35mAPOSTA DO COMPUTADOR: {chuteComputador}\033[0;0m')

            time.sleep(2)
            dadoSorteado = random.randint(1, 1)
            print(f'\033[1;33mVALOR SORTEADO: {dadoSorteado}\033[0;0m')
            time.sleep(1)


            if chuteUsuario == dadoSorteado:
                print(f'\033[1;32m\n','='*10,'VOCÊ GANHOU','='*10,'\n\n\033[0;00m')
                self.valor += 4
                time.sleep(1)
                qnt = 51- len(str(self.valor)) - 10
                print(f'\033[1;35mCRÉDITOS: {self.valor}','='*qnt,'\033[0;0m')
                
                if revanche:
                    break
                dobrar = [
                    inquirer.List(
                        'escolha',
                        message= f'\033[1;36mVAMOS DOBRAR A APOSTA?\nSe você ganhar...leva R$8,00, se perder...me devolve os R$4,00\033[0;00m',
                        choices = ('SIM', 'NÃO'))        
                ]
                
                dobra = inquirer.prompt(dobrar)['escolha']
                
                if dobra == 'SIM':
                    qnt = 51- len(str(self.valor)) - 10
                    print(f'\033[1;35mCRÉDITOS: {self.valor - 4}','='*qnt,'\033[0;0m')
                    revanche = True
                
                elif dobra=='NÃO':
                    print(f'\033[1;33mOK ENTÃO!\033[0;0m')
                    break

            elif chuteComputador == dadoSorteado:
                print(f'\033[1;31m\n','='*10,'VOCÊ PERDEU','='*10,'\n\n\033[0;00m')
                if revanche == True:
                    self.valor -= 4
                break


    def sacar(self):
        sacar =  [
        inquirer.List(
            'escolha',
            message= f'\033[1;36mSACAR CRÉDITOS RESTANTES? \033[0;0m',
            choices= ('SIM', 'NÃO'))
        ]
        sacarCreditos = inquirer.prompt(sacar)['escolha']

        if sacarCreditos == 'SIM':
            self.valor = 0 

            qnt = 51- len(str(self.valor)) - 10
            print(f'\033[1;35mCRÉDITOS: {self.valor}','='*qnt,'\033[0;0m')
            print(f'\033[1;33mATÉ A PRÓXIMA!\033[0;0m')

        elif sacarCreditos == 'NÃO':
            print(f'\033[1;33mATÉ A PRÓXIMA!\033[0;0m')
            
