def numBinario():
    binX = list(input("BINARY NUMBER:\n"))
    value = 0

    for i in range(len(binX)):
        num = binX.pop()
        if num == '1':
            value = value + pow(2, i)
    print("The decimal value of the number is:", value)



    decX = int(input("DECIMAL NUMBER:\n"))
    value = 0

    for j in range(1, decX):
        num = decX // 2
        # num = decX.pop()
        # if num >=1:
        #     value = value +


if __name__ == '__main__':
    numBinario()




