import random

import winsound
from PyQt5 import QtCore, QtGui, QtWidgets


class Jokenpo(object):
    def setupUi(self, Form):
        winsound.PlaySound("../songs/marioBowserCastle_Jokenpo.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
        Form.setObjectName("Form")
        Form.resize(1280, 720)

        self.placarY = 0
        self.placarP = 0

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../backgrounds/Jokenpo.png"))
        self.label.setObjectName("label")

        self.imgSorteada = QtWidgets.QLabel(Form)
        self.imgSorteada.setGeometry(QtCore.QRect(260, 270, 120, 120))
        self.imgSorteada.setStyleSheet("background-color: rgb(0,0,0,0%)")

        self.placar = QtWidgets.QLabel(Form)
        self.placar.setGeometry(QtCore.QRect(1000, 620, 120, 95))
        self.placar.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.placar.setPixmap(QtGui.QPixmap("../elements/youPC.png"))

        self.placarYou = QtWidgets.QLabel(Form)
        self.placarYou.setGeometry(QtCore.QRect(1125, 620, 50, 45))
        self.placarYou.setStyleSheet("background-color: rgb(0,0,0,0%); color: #FCCF00; font-size: 36px; font: bold;")
        self.placarYou.setText("0")

        self.placarPC = QtWidgets.QLabel(Form)
        self.placarPC.setGeometry(QtCore.QRect(1125, 670, 50, 45))
        self.placarPC.setStyleSheet("background-color: rgb(0,0,0,0%); color: #009BD9; font-size: 36px; font: bold;")
        self.placarPC.setText("0")


        self.btnMario = QtWidgets.QPushButton(Form)
        self.btnMario.setGeometry(QtCore.QRect(160, 520, 91, 71))
        self.btnMario.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnMario.setText("")
        self.btnMario.setObjectName("btnMario")
        self.btnMario.clicked.connect(lambda: self.comparacao(0))

        self.btnPeach = QtWidgets.QPushButton(Form)
        self.btnPeach.setGeometry(QtCore.QRect(280, 480, 91, 71))
        self.btnPeach.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnPeach.setText("")
        self.btnPeach.setObjectName("btnPeach")
        self.btnPeach.clicked.connect(lambda: self.comparacao(1))

        self.btnBowser = QtWidgets.QPushButton(Form)
        self.btnBowser.setGeometry(QtCore.QRect(400, 500, 91, 71))
        self.btnBowser.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnBowser.setText("")
        self.btnBowser.setObjectName("btnBowser")
        self.btnBowser.clicked.connect(lambda: self.comparacao(2))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.guardar = 3
        self.sortear()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def sortear(self):
        self.img = random.randint(0, 2)

        while True:
            if self.img == self.guardar:
                self.img = random.randint(0, 2)
            else:
                break

        if self.img == 0:
            self.imgSorteada.setPixmap(QtGui.QPixmap("../elements/marioJ.png"))
        if self.img == 1:
            self.imgSorteada.setPixmap(QtGui.QPixmap("../elements/peachJ.png"))
        if self.img == 2:
            self.imgSorteada.setPixmap(QtGui.QPixmap("../elements/browserJ.png"))

        self.guardar = self.img


    def comparacao(self, escolha):
        if escolha == self.img:
            self.ganhou = False
            self.placarP += 1

        elif escolha == 0 and self.img == 2:
            self.ganhou = True
            self.placarY += 1
            print("-------mario")

        elif escolha == 1 and self.img == 0:
            self.ganhou = True
            self.placarY += 1
            print("-------peach")

        elif escolha == 2 and self.img == 1:
            self.ganhou = True
            self.placarY += 1
            print("-------browser")

        else:
            self.ganhou = False
            self.placarP += 1

        self.placarYou.setText(str(self.placarY))
        self.placarPC.setText(str(self.placarP))

        self.sortear()

        print(self.ganhou)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Jokenpo()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
