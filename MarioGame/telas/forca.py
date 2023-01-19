from PyQt5 import QtCore, QtGui, QtWidgets
import random
import os


class Forca(object):
    def setupUi(self, Form):
        Form.setObjectName("Forca")
        Form.resize(1280, 720)

        self.letrasE = []
        self.letrasC = []
        self.letrasT = []

        self.backgrondForca = QtWidgets.QLabel(Form)
        self.backgrondForca.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.backgrondForca.setText("")
        self.backgrondForca.setPixmap(QtGui.QPixmap("../backgrounds/Forca0.png"))
        self.backgrondForca.setObjectName("bgForca")

        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.result.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.result.hide()

        self.word = QtWidgets.QLabel(Form)
        self.word.setGeometry(QtCore.QRect(325, 290, 850, 100))
        self.word.setStyleSheet("background-color: rgb(0,0,0,0%); color: #ffffff; font-size: 85px;")
        self.word.setText("")

        self.tema = QtWidgets.QLabel(Form)
        self.tema.setGeometry(QtCore.QRect(10, 528, 190, 30))
        self.tema.setStyleSheet("background-color: rgb(0,0,0,0%); color: #ff0000; font-size: 17px; font:bold;")
        self.tema.setText("")

        self.btnQuit = QtWidgets.QPushButton(Form)
        self.btnQuit.setGeometry(QtCore.QRect(1160, 30, 85, 30))
        self.btnQuit.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btnQuit.setStyleSheet("border-image: url(../elements/quitt.png);")
        self.btnQuit.clicked.connect(self.quit)

        self.btn_Q = QtWidgets.QPushButton(Form)
        self.btn_Q.setGeometry(QtCore.QRect(219, 570, 40, 40))
        self.btn_Q.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_Q.setObjectName("btn_Q")
        self.btn_Q.clicked.connect(lambda: self.verificarLetra("Q", self.btn_Q))

        self.btn_W = QtWidgets.QPushButton(Form)
        self.btn_W.setGeometry(QtCore.QRect(300, 570, 40, 40))
        self.btn_W.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_W.setObjectName("btn_W")
        self.btn_W.clicked.connect(lambda: self.verificarLetra("W", self.btn_W))

        self.btn_E = QtWidgets.QPushButton(Form)
        self.btn_E.setGeometry(QtCore.QRect(400, 570, 40, 40))
        self.btn_E.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_E.setObjectName("btn_E")
        self.btn_E.clicked.connect(lambda: self.verificarLetra("E", self.btn_E))

        self.btn_R = QtWidgets.QPushButton(Form)
        self.btn_R.setGeometry(QtCore.QRect(490, 570, 40, 40))
        self.btn_R.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_R.setObjectName("btn_R")
        self.btn_R.clicked.connect(lambda: self.verificarLetra("R", self.btn_R))

        self.btn_T = QtWidgets.QPushButton(Form)
        self.btn_T.setGeometry(QtCore.QRect(580, 570, 40, 40))
        self.btn_T.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_T.setObjectName("btn_T")
        self.btn_T.clicked.connect(lambda: self.verificarLetra("T", self.btn_T))

        self.btn_Y = QtWidgets.QPushButton(Form)
        self.btn_Y.setGeometry(QtCore.QRect(670, 570, 40, 40))
        self.btn_Y.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_Y.setObjectName("btn_Y")
        self.btn_Y.clicked.connect(lambda: self.verificarLetra("Y", self.btn_Y))

        self.btn_U = QtWidgets.QPushButton(Form)
        self.btn_U.setGeometry(QtCore.QRect(760, 570, 40, 40))
        self.btn_U.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_U.setObjectName("btn_U")
        self.btn_U.clicked.connect(lambda: self.verificarLetra("U", self.btn_U))

        self.btn_I = QtWidgets.QPushButton(Form)
        self.btn_I.setGeometry(QtCore.QRect(840, 570, 40, 40))
        self.btn_I.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_I.setObjectName("btn_I")
        self.btn_I.clicked.connect(lambda: self.verificarLetra("I", self.btn_I))

        self.btn_O = QtWidgets.QPushButton(Form)
        self.btn_O.setGeometry(QtCore.QRect(930, 570, 40, 40))
        self.btn_O.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_O.setObjectName("btn_O")
        self.btn_O.clicked.connect(lambda: self.verificarLetra("O", self.btn_O))

        self.btn_A = QtWidgets.QPushButton(Form)
        self.btn_A.setGeometry(QtCore.QRect(260, 620, 40, 40))
        self.btn_A.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_A.setObjectName("btn_A")
        self.btn_A.clicked.connect(lambda: self.verificarLetra("A", self.btn_A))

        self.btn_S = QtWidgets.QPushButton(Form)
        self.btn_S.setGeometry(QtCore.QRect(350, 620, 40, 40))
        self.btn_S.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_S.setObjectName("btn_S")
        self.btn_S.clicked.connect(lambda: self.verificarLetra("S", self.btn_S))

        self.btn_D = QtWidgets.QPushButton(Form)
        self.btn_D.setGeometry(QtCore.QRect(440, 620, 40, 40))
        self.btn_D.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_D.setObjectName("btn_D")
        self.btn_D.clicked.connect(lambda: self.verificarLetra("D", self.btn_D))

        self.btn_F = QtWidgets.QPushButton(Form)
        self.btn_F.setGeometry(QtCore.QRect(530, 620, 40, 40))
        self.btn_F.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_F.setObjectName("btn_F")
        self.btn_F.clicked.connect(lambda: self.verificarLetra("F", self.btn_F))

        self.btn_G = QtWidgets.QPushButton(Form)
        self.btn_G.setGeometry(QtCore.QRect(620, 620, 40, 40))
        self.btn_G.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_G.setObjectName("btn_G")
        self.btn_G.clicked.connect(lambda: self.verificarLetra("G", self.btn_G))

        self.btn_H = QtWidgets.QPushButton(Form)
        self.btn_H.setGeometry(QtCore.QRect(710, 620, 40, 40))
        self.btn_H.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_H.setObjectName("btn_H")
        self.btn_H.clicked.connect(lambda: self.verificarLetra("H", self.btn_H))

        self.btn_J = QtWidgets.QPushButton(Form)
        self.btn_J.setGeometry(QtCore.QRect(800, 620, 40, 40))
        self.btn_J.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_J.setObjectName("btn_J")
        self.btn_J.clicked.connect(lambda: self.verificarLetra("J", self.btn_J))

        self.btn_K = QtWidgets.QPushButton(Form)
        self.btn_K.setGeometry(QtCore.QRect(890, 620, 40, 40))
        self.btn_K.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_K.setObjectName("btn_K")
        self.btn_K.clicked.connect(lambda: self.verificarLetra("K", self.btn_K))

        self.btn_L = QtWidgets.QPushButton(Form)
        self.btn_L.setGeometry(QtCore.QRect(980, 620, 40, 40))
        self.btn_L.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_L.setObjectName("btn_L")
        self.btn_L.clicked.connect(lambda: self.verificarLetra("L", self.btn_L))

        self.btn_Z = QtWidgets.QPushButton(Form)
        self.btn_Z.setGeometry(QtCore.QRect(310, 670, 40, 40))
        self.btn_Z.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_Z.setObjectName("btn_Z")
        self.btn_Z.clicked.connect(lambda: self.verificarLetra("Z", self.btn_Z))

        self.btn_X = QtWidgets.QPushButton(Form)
        self.btn_X.setGeometry(QtCore.QRect(400, 670, 40, 40))
        self.btn_X.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_X.setObjectName("btn_X")
        self.btn_X.clicked.connect(lambda: self.verificarLetra("X", self.btn_X))

        self.btn_C = QtWidgets.QPushButton(Form)
        self.btn_C.setGeometry(QtCore.QRect(490, 670, 40, 40))
        self.btn_C.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_C.setObjectName("btn_C")
        self.btn_C.clicked.connect(lambda: self.verificarLetra("C", self.btn_C))

        self.btn_V = QtWidgets.QPushButton(Form)
        self.btn_V.setGeometry(QtCore.QRect(580, 670, 40, 40))
        self.btn_V.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_V.setObjectName("btn_V")
        self.btn_V.clicked.connect(lambda: self.verificarLetra("V", self.btn_V))

        self.btn_B = QtWidgets.QPushButton(Form)
        self.btn_B.setGeometry(QtCore.QRect(670, 670, 40, 40))
        self.btn_B.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_B.setObjectName("btn_B")
        self.btn_B.clicked.connect(lambda: self.verificarLetra("B", self.btn_B))

        self.btn_N = QtWidgets.QPushButton(Form)
        self.btn_N.setGeometry(QtCore.QRect(750, 670, 40, 40))
        self.btn_N.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_N.setObjectName("btn_N")
        self.btn_N.clicked.connect(lambda: self.verificarLetra("N", self.btn_N))

        self.btn_M = QtWidgets.QPushButton(Form)
        self.btn_M.setGeometry(QtCore.QRect(840, 670, 40, 40))
        self.btn_M.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_M.setObjectName("btn_M")
        self.btn_M.clicked.connect(lambda: self.verificarLetra("M", self.btn_M))

        self.btn_P = QtWidgets.QPushButton(Form)
        self.btn_P.setGeometry(QtCore.QRect(1020, 570, 40, 40))
        self.btn_P.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_P.setObjectName("btn_P")
        self.btn_P.clicked.connect(lambda: self.verificarLetra("P", self.btn_P))

        self.btn_Enter = QtWidgets.QPushButton(Form)
        self.btn_Enter.setGeometry(QtCore.QRect(940, 679, 61, 31))
        self.btn_Enter.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btn_Enter.setObjectName("btn_Enter")

        self.principal1()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.allLetters = [self.btn_Q, self.btn_W, self.btn_E, self.btn_R, self.btn_T, self.btn_Y, self.btn_U,
                           self.btn_I, self.btn_O, self.btn_P, self.btn_A, self.btn_S, self.btn_D, self.btn_F,
                           self.btn_G, self.btn_H, self.btn_J, self.btn_K, self.btn_L, self.btn_Z, self.btn_X,
                           self.btn_C, self.btn_V, self.btn_B, self.btn_N, self.btn_M]

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def principal1(self):
        pasta = './'
        temas = []
        for x in os.walk(pasta):
            for y in x:
                if y.__contains__('carros.txt'):
                    for z in y:
                        if z.__contains__('.txt'):
                            temas.append(z)
                    break

        print("temas: ", temas)
        tema = random.choice(temas)
        print(tema)
        temaa = tema.replace(".txt", "").replace("_", " ")

        self.tema.setText("THEME: " + temaa)
        arq = open(tema, "r", encoding="utf-8")
        txtarq = arq.read()
        palavra = ''
        lista = []
        for i in txtarq:
            if i != ",":
                palavra += i
            else:
                lista.append(palavra)
                palavra = ''
        # self.palavraSorteada = random.choice(lista)
        self.palavraSorteada = 'a'
        print(self.palavraSorteada)
        arq.close()
        vazio = "_ " * len(self.palavraSorteada)
        self.word.setText(vazio)
        self.forcaIMG = ["../backgrounds/Forca0.png", "../backgrounds/Forca1.png", "../backgrounds/Forca2.png",
                         "../backgrounds/Forca3.png", "../backgrounds/Forca4.png", "../backgrounds/Forca5.png"]

    def verificarLetra(self, palpite, btn=""):
        if btn != "":
            btn.setEnabled(False)

        print(palpite)
        # self.allLetters[palpite].setDisabled(False)
        temaletra = False
        for i in self.palavraSorteada:
            if i.upper() == palpite:
                temaletra = True

        if temaletra:
            self.letrasT.append(palpite)
            self.letrasC.append(palpite)

        else:
            self.letrasT.append(palpite)
            self.letrasE.append(palpite)

        verificador = 0
        img = self.forcaIMG[len(self.letrasE)]
        self.backgrondForca.setPixmap(QtGui.QPixmap(img))

        if len(self.letrasE) >= 5:
            print(f'\nPERDEU:) a palavra é {self.palavraSorteada}')
            self.word.hide()
            self.result.show()
            self.tema.hide()
            self.result.setPixmap(QtGui.QPixmap("../backgrounds/gameOverR.png"))
            return
        palavra = ""
        for i in self.palavraSorteada:
            hide = True
            for j in self.letrasT:
                if i.upper() == j.upper():
                    print(f'\033[1;97m', i.upper(), end="")
                    palavra += i.upper()
                    palavra += " "
                    verificador += 1
                    hide = False
            if hide:
                palavra += "_ "
                print('-', end="")
        print("ppp", palavra)
        self.word.setText(palavra)

        if len(self.palavraSorteada) == verificador:
            print("\nGANHOU")
            self.word.hide()
            self.result.show()
            self.tema.hide()
            self.result.setPixmap(QtGui.QPixmap("../backgrounds/congratulationsR.png"))
            return

        letras = str(self.letrasT)
        letras = letras.replace('[', '')
        letras = letras.replace(']', '')
        letras = letras.replace("'", '')

        print("\nLETRAS DIGITADAS: ", letras)
        print(f'\033[1;35m-_' * 20, '\n\033[0;0m')

    def quit(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Forca()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
