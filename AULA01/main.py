
def data():
    dia = int(input('''Entre com sua data de nascimento
    Dia: '''))
    mes = int(input(f'Mês: '))
    ano = int(input(f'Ano: '))
    if (ano < 2004):
        print(f'Pode tirar sua CNH')

    elif (ano == 2004 and mes < 8):
        print(f'Pode tirar sua CNH')

    elif (ano == 2004 and mes == 8 and dia <= 11):
        print(f'pode tirar sua CNH')

    else:
        print(f'Ainda não pode tirar CNH');