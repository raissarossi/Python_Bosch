def contarLetras(string):
    dicioQ = dict()
    dicioP = dict()
    ultimaPosi = 0
    for i in string:
        if dicioQ.__contains__(i):
            dicioQ[i] += 1
            dicioP[i] += [ultimaPosi]
        else:
            dicioQ[i] = 1
            dicioP[i] = [ultimaPosi]
        # ultimaPosi = string.find('s', ultimaPosi)+1
        ultimaPosi += 1
    return dicioQ, dicioP
def formatar(dicioQ, dicioP):
    novoDicioQ = str(dicioQ)
    novoDicioP = str(dicioP)
    novoDicioQ = novoDicioQ.replace("{", "")
    novoDicioQ = novoDicioQ.replace("}", " VEZES")
    novoDicioQ = novoDicioQ.replace(", ", " VEZES\n")
    novoDicioQ = novoDicioQ.replace(":", " FOI DIGITADO:")
    # print(novoDicioQ)
    novoDicioP = novoDicioP.replace("{", "")
    novoDicioP = novoDicioP.replace("}", "")
    novoDicioP = novoDicioP.replace(", '", "\n'")
    novoDicioP = novoDicioP.replace(":", " FOI DIGITADO NAS POSIÇÕES:")
    # print(novoDicioP)
    return novoDicioQ, novoDicioP

def alternado(strQ, strP):
    ultimaPosi = 0
    for i in strQ:
        print(i, end="")
        if i == "S":
            print("")
            for j in strP[ultimaPosi:]:
                print(j, end="")
                if j == "]":
                    # ultimaPosi = string.find('[', ultimaPosi)
                    ultimaPosi = ultimaPosi + 1
                    print("")
                    break

if __name__ == '__main__':
    dQ, dP = contarLetras("pythonetscampinas")
    nDQ, nDP = formatar(dQ, dP)
    alternado(nDQ, nDP)
