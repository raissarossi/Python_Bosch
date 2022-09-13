def numBinario():
    binX = list(input("BINARY NUMBER:\n"))
    value = 0

    for i in range(len(binX)):
        num = binX.pop()
        if num != '0':
            if num != '1':
                print("ERRO")
                break

        if num == '1':
            value = value + pow(2, i)
    print("The decimal value of the number is:", value)

if __name__ == '__main__':
    numBinario()





