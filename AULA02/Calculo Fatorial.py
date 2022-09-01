def main():
    number = int(input("TYPE A NUMBER:\n"))
    contador = 1
    fat = 1

    while (contador<= number):
        fat = fat*contador
        contador = contador + 1
    print(f'The factorization of {number} is {fat}')
main()
