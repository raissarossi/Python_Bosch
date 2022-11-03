import inquirer
from creditos import Creditos

dinheiro = Creditos()
valorCredito = dinheiro.depositarCreditos()

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
            print(f'\033[1;31mCRÉDITOS INSUFICIENTES: {dinheiro.valor}\033[0;0m')
            depositar = [
                    inquirer.List(
                        'escolha',
                        message= f'\033[1;36mDEPOSITAR MAIS CRÉDITOS?\033[0;00m',
                        choices = ('SIM', 'SAIR'))        
                    ]
            deposito = inquirer.prompt(depositar)['escolha']
            if deposito == 'SIM':
                print('\033[1;33mVAMOS LÁ\033[0;0m')
                valorCredito = dinheiro.depositarCreditos()
            elif deposito == 'SAIR':
                break
            else:
                pass

        dinheiro.valor -= 2
        print(f'\033[1;35mCRÉDITOS: {dinheiro.valor}\033[0;0m')
        dinheiro.jogoDados()
        jogarDnv = [
                    inquirer.List(
                        'escolha',
                        message= f'\033[1;36mJOGAR NOVAMENTE?\033[0;0m',
                        choices = ('SIM', 'NÃO'))        
                    ]
        jogarNovamente = inquirer.prompt(jogarDnv)['escolha']
        if jogarNovamente == 'SIM':
            print('\033[1;33mVAMOS LÁ\033[0;0m')
        elif jogarNovamente == 'NÃO':
            break

elif inicio == 'NÃO':
    print(f'\033[1;35mCRÉDITOS: {dinheiro.valor}')
    sacar =  [
    inquirer.List(
        'escolha',
        message= f'\033[1;36mSACAR CRÉDITOS RESTANTES? \033[0;0m',
        choices= ('SIM', 'NÃO'))
    ]
    sacarCreditos = inquirer.prompt(sacar)['escolha']
    if sacarCreditos == 'SIM':
        dinheiro.valor = 0 
        print(f'\033[1;35mCRÉDITOS: {dinheiro.valor}\033[0;0m')
        print('\033[1;33mATÉ A PRÓXIMA!\033[0;0m')
    elif sacarCreditos == 'NÃO':
        print('\033[1;33mATÉ A PRÓXIMA!\033[0;0m')

