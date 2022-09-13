def formas():
    #SOLID SQUARE
    x = int(input("NUMBER:\n"))
    tam = x
    # altura = x
    for _ in range(tam):
        print('.  ' * tam)
    print("\n")

    altura = x
    largura = x
    preenchimento = "   "
    larg = largura-2
    pree = preenchimento * (larg)
    preen = 1

    print('.  ' * largura)
    for _ in range(altura-2):
        print(f".  {pree}.")
    print('.  ' * largura)
    print("\n")

    for _ in range(1, x + 1):
        print(_ * '.  ')
    print("\n")

    for _ in range(1, x + 1):
        print('.  ',preen,'.')
    print('.  '* largura)


if __name__ == '__main__':
    formas()