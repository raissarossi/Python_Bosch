import inquirer
import random

class Creditos:
    def __init__(self):
        self.valor = 0
    
    def depositarCreditos(self):
        valorvalor = int(input("INSIRA O VALOR DESEJADO:\n"))
        # print(valorvalor)
        self.valor += valorvalor
        print('SEUS CRÉDITOS FORAM ADICIONADOS\n')
        print(f'CRÉDITOS: {self.valor}')
    
    def jogoDados(self):
        chuteUser = [
            inquirer.List(
                'escolha',
                message= f'\033[1;36mSEU CHUTE\033[0;00m',
                choices = (1, 2, 3, 4, 5, 6))        
            ]
        dadoSorteado = random.randint(1, 1)
        print(dadoSorteado)
        chuteUsuario = inquirer.prompt(chuteUser)['escolha']
        
        print(chuteUsuario)
        if chuteUsuario == dadoSorteado:
            print(f'\033[1;32mVOCÊ GANHOU\033[0;00m')
            self.valor += 4
            print(f'CRÉDITOS: {self.valor}')
            dobrar = [
                inquirer.List(
                    'escolha',
                    message= f'\033[1;36mVAMOS DOBRAR A APOSTA?\nSe você ganhar...leva R$8,00, se perder...me devolve os R$4,00\033[0;00m',
                    choices = ('SIM', 'SAIR'))        
            ]

        else:
            print(f'\033[1;31mVOCÊ PERDEU\033[0;00m')

        

            
