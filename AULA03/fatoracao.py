def fatoracao():
    number = int(input("TYPE A NUMBER:\n"))
    result = 1
    for fat in range(1,number+1):
        result *= fat
    print(result)

if __name__ == '__main__':
    fatoracao()

