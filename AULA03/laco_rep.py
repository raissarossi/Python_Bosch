import random
def laco_rep_for():
    r = list(range(0,10,3))
    print(r)

    temperatura = [10, 15, 20, 25, 30, 35, 40]
    for t in temperatura:
      print(t)



    aprendizes = ["Beltrana", "Ciclano", "Fulano", "Marcão", "Neymar"]
    notas = [9, 3, 7, 10, 5]
    notass = random.randint(0,10)
    for pos in range(5):
        print(aprendizes[pos],notas[pos])



    for c in range(0,10):
        print(c, end='\t')
    print()

    for c in range(1,11,3):
        print(c,end=' ')








if __name__ == '__main__':
    laco_rep_for()