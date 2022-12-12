from PyQt5 import QtWidgets

from jogo_da_velha import Ui_jogo_da_velha

class Configuracao_Jogo_da_Velha(Ui_jogo_da_velha):
    def __init__(self, jogo_da_velha):
        self.setupUi(jogo_da_velha)
        self.marca = 'O'
        self.velha = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]
        self.player = 10

        self.btn_1.clicked.connect(self.alteracao1)
        self.btn_2.clicked.connect(self.alteracao2)
        self.btn_3.clicked.connect(self.alteracao3)
        self.btn_4.clicked.connect(self.alteracao4)
        self.btn_5.clicked.connect(self.alteracao5)
        self.btn_6.clicked.connect(self.alteracao6)
        self.btn_7.clicked.connect(self.alteracao7)
        self.btn_8.clicked.connect(self.alteracao8)
        self.btn_9.clicked.connect(self.alteracao9)

    def players(self):
        if self.player == 10:
            self.player = 20
            self.marca = 'X'
        else:
            self.player = 10
            self.marca = 'O'
        self.winner()
        print(self.velha)

    def alteracao1(self):
        self.velha[0][0] = self.player
        self.btn_1.setText(self.marca)
        self.btn_1.setEnabled(False)
        self.players()


    def alteracao2(self):
        self.velha[0][1] = self.player
        self.btn_2.setText(self.marca)
        self.btn_2.setEnabled(False)
        self.players()

    def alteracao3(self):
        self.velha[0][2] = self.player
        self.btn_3.setText(self.marca)
        self.btn_3.setEnabled(False)
        self.players()

    def alteracao4(self):
        self.velha[1][0] = self.player
        self.btn_4.setText(self.marca)
        self.btn_4.setEnabled(False)
        self.players()

    def alteracao5(self):
        self.velha[1][1] = self.player
        self.btn_5.setText(self.marca)
        self.btn_5.setEnabled(False)
        self.players()

    def alteracao6(self):
        self.velha[1][2] = self.player
        self.btn_6.setText(self.marca)
        self.btn_6.setEnabled(False)
        self.players()

    def alteracao7(self):
        self.velha[2][0] = self.player
        self.btn_7.setText(self.marca)
        self.btn_7.setEnabled(False)
        self.players()

    def alteracao8(self):
        self.velha[2][1] = self.player
        self.btn_8.setText(self.marca)
        self.btn_8.setEnabled(False)
        self.players()

    def alteracao9(self):
        self.velha[2][2] = self.player
        self.btn_9.setText(self.marca)
        self.btn_9.setEnabled(False)
        self.players()

    def winner(self):
        resto = False
        l0 = self.velha[0]
        l1 = self.velha[1]
        l2 = self.velha[2]
        c0 = [self.velha[0][0], self.velha[1][0], self.velha[2][0]]
        c1 = [self.velha[0][1], self.velha[1][1], self.velha[2][1]]
        c2 = [self.velha[0][2], self.velha[1][2], self.velha[2][2]]
        d0 = [self.velha[0][0], self.velha[1][1], self.velha[2][2]]
        d1 = [self.velha[0][2], self.velha[1][1], self.velha[2][0]]
        tudo = [l0, l1, l2, c0, c1, c2, d0, d1]
        valorX = [10, 10, 10]
        valorO = [20, 20, 20]
        for i in tudo:
            if i == valorX:
                print("O ganhou:)")

                return
            if i == valorO:
                print("X ganhou:)")
                return
        for i in self.velha:
            for j in i:
                if not(j != 10 or j != 20):
                    resto = True
                    print("Velhaaaaaaa")
                    return


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    jogo_da_velha = QtWidgets.QMainWindow()
    config_jogo_da_velha = Configuracao_Jogo_da_Velha(jogo_da_velha)
    jogo_da_velha.show()

    app.exec()