def pedirConta():
    conta = input('[S] para sair ou insira a conta: ').upper()
    if conta =='S':
        print('Saindo')
    conta = verifichar(conta)
    if "+" in conta:
        somar(conta)
    elif "-" in conta:
        conta.removeprefix('-')
        sub(conta)
    elif "*" in conta:
        mult(conta)
    elif "/" in conta:
        div(conta)


def somar(conta):
    sub = conta.split("+")
    if conta[0] =='+':
        result = +int(sub[1]) + int(sub[2])
    else:
        result = int(sub[0]) + int(sub[1])


def sub(conta):
    sub = conta.split("-")
    if conta[0] =='-':
        result = -int(sub[1]) - int(sub[2])
    else:
        result = int(sub[0]) - int(sub[1])
        print(result)

def mult(conta):
    mult = conta.split("*")
    result = int(mult[0]) * int(mult[1])
    print(result)

def div(conta):
    div = conta.split("/")
    result = int(div[0]) / int(div[1])
    print(result)


def verifichar(conta):
    char_operacao = ['+', '-', '*', '/']
    char_letra = ['G', 'R', 'M', 'H']
    for i in range(len(char_letra)):
        if conta[0] == char_letra[i]:
            conta.removeprefix(char_letra[i-1])
        else: pass
    return conta

    for i in range(len(char_operacao)):
        if char_letra[i] in conta.strip().upper():
            char = char_letra[i]
        else:
            char ='y'

    for i in range(len(char_operacao)):
        if char_operacao[i] in conta.strip().upper():
            print(f"Funcionou, o char é {char}")
            return True, char
        else:
            return False

if __name__ == '__main__':
    pedirConta()