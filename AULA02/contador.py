def lacoInfinito():
    contador = 0
    while True:
        contador += 1
        if contador % 5 == 0:
            continue
        print(contador)
        if contador > 50:
            break


if __name__ == '__main__':
    print("COMEÇANDO...")
    lacoInfinito()
