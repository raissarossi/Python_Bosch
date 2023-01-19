import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5 import uic, QtGui

class TicTacToe(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 720)
        self.scoreMario = 0
        self.scoreToad = 0
        self.player = 2

        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, -1, 1280, 720))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../backgrounds/TicTacToePorta.png"))
        self.background.setObjectName("background")

        self.lblMario = QtWidgets.QLabel(Form)
        self.lblMario.setGeometry(QtCore.QRect(275, 600, 70, 40))
        self.lblMario.setText("0")
        self.lblMario.setStyleSheet("font-size:40px; color: #ffffff; font: bold;")
        self.lblMario.hide()

        self.lblToad = QtWidgets.QLabel(Form)
        self.lblToad.setGeometry(QtCore.QRect(1120, 598, 70, 40))
        self.lblToad.setText("0")
        self.lblToad.setStyleSheet("font-size:40px; color: #ffffff; font: bold;")
        self.lblToad.hide()

        self.btnReset = QtWidgets.QPushButton(Form)
        self.btnReset.setGeometry(QtCore.QRect(585, 650, 120, 30))
        self.btnReset.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btnReset.setStyleSheet("border-image: url(../elements/reset.png);")
        self.btnReset.setDisabled(True)
        self.btnReset.hide()
        self.btnReset.clicked.connect(self.reset)

        self.bgResult = QtWidgets.QLabel(Form)
        self.bgResult.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.bgResult.setStyleSheet("background-color: rgb(0,0,0,50%)")
        self.bgResult.hide()

        self.btnQuit = QtWidgets.QPushButton(Form)
        self.btnQuit.setGeometry(QtCore.QRect(1160, 30, 85, 30))
        self.btnQuit.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btnQuit.setStyleSheet("border-image: url(../elements/quit.png);")
        self.btnQuit.clicked.connect(self.quit)

        self.btnDoor = QtWidgets.QPushButton(Form)
        self.btnDoor.setGeometry(QtCore.QRect(580, 230, 121, 101))
        self.btnDoor.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnDoor.setText("")
        self.btnDoor.setObjectName("btnDoor")
        self.btnDoor.clicked.connect(self.startPorta)

        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(430, 193, 135, 135))
        self.pushButton_1.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("1")
        self.pushButton_1.setDisabled(True)
        self.pushButton_1.clicked.connect(lambda: self.verificarNum(1))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(575, 193, 135, 135))
        self.pushButton_2.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("2")
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.clicked.connect(lambda: self.verificarNum(2))
        self.pushButton_2.hide()

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 193, 135, 135))
        self.pushButton_3.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("3")
        self.pushButton_3.setDisabled(True)
        self.pushButton_3.clicked.connect(lambda: self.verificarNum(3))

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 337, 135, 135))
        self.pushButton_4.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("4")
        self.pushButton_4.setDisabled(True)
        self.pushButton_4.clicked.connect(lambda: self.verificarNum(4))

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(575, 337, 135, 135))
        self.pushButton_5.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("5")
        self.pushButton_5.setDisabled(True)
        self.pushButton_5.clicked.connect(lambda: self.verificarNum(5))

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(720, 337, 135, 135))
        self.pushButton_6.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("6")
        self.pushButton_6.setDisabled(True)
        self.pushButton_6.clicked.connect(lambda: self.verificarNum(6))

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(430, 480, 135, 135))
        self.pushButton_7.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("7")
        self.pushButton_7.setDisabled(True)
        self.pushButton_7.clicked.connect(lambda: self.verificarNum(7))

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(575, 480, 135, 135))
        self.pushButton_8.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("8")
        self.pushButton_8.setDisabled(True)
        self.pushButton_8.clicked.connect(lambda: self.verificarNum(8))

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(720, 480, 135, 135))
        self.pushButton_9.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("9")
        self.pushButton_9.setDisabled(True)
        self.pushButton_9.clicked.connect(lambda: self.verificarNum(9))

        self.btnP = [self.pushButton_1, self.pushButton_2, self.pushButton_3,
                     self.pushButton_4, self.pushButton_5, self.pushButton_6,
                     self.pushButton_7, self.pushButton_8, self.pushButton_9]

        for i in self.btnP:
            i.setText("0")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def startPorta(self):
        print("ok")
        self.btnDoor.setDisabled(True)
        self.btnDoor.hide()
        self.lblMario.show()
        self.lblToad.show()
        self.pushButton_2.show()
        self.btnReset.show()
        self.pushButton_1.setDisabled(False)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)
        self.pushButton_7.setDisabled(False)
        self.pushButton_8.setDisabled(False)
        self.pushButton_9.setDisabled(False)
        self.background.setPixmap(QtGui.QPixmap("../backgrounds/TicTacToe.png"))

    def verificarNum(self, number):
        self.btnReset.setDisabled(True)
        number -= 1
        print(number)
        if self.player == 1:
            self.icon = "border-image: url(../elements/green.png);color: rgb(0,0,0,0%);"
            self.player = 2
        else:
            self.icon = "border-image: url(../elements/red.png);color: rgb(0,0,0,0%);"
            self.player = 1

        self.btnP[number].setStyleSheet(self.icon)
        self.btnP[number].setText(str(self.player))
        print(self.btnP[number].text())
        self.btnP[number].setEnabled(False)
        if self.verify():
            print("cabo")

    def verify(self):
        print("passou")
        l0 = [self.btnP[0].text(), self.btnP[1].text(), self.btnP[2].text()]
        l1 = [self.btnP[3].text(), self.btnP[4].text(), self.btnP[5].text()]
        l2 = [self.btnP[6].text(), self.btnP[7].text(), self.btnP[8].text()]

        c0 = [self.btnP[0].text(), self.btnP[3].text(), self.btnP[6].text()]
        c1 = [self.btnP[1].text(), self.btnP[4].text(), self.btnP[7].text()]
        c2 = [self.btnP[2].text(), self.btnP[5].text(), self.btnP[8].text()]

        d0 = [self.btnP[0].text(), self.btnP[4].text(), self.btnP[8].text()]
        d1 = [self.btnP[2].text(), self.btnP[4].text(), self.btnP[6].text()]

        tudo = [l0, l1, l2, c0, c1, c2, d0, d1]

        for i in tudo:
            if i == ["1", "1", "1"]:
                print("mario")
                self.scoreMario += 1
                self.lblMario.setText(str(self.scoreMario))
                self.stop(True)
                self.btnReset.setDisabled(False)
                if self.scoreMario >= 5:
                    self.reset()
                    self.bgResult.show()
                    self.bgResult.setPixmap(QtGui.QPixmap("../backgrounds/congratulationsW.png"))
                return True

            if i == ["2", "2", "2"]:
                print("toad")
                self.scoreToad += 1
                self.lblToad.setText(str(self.scoreToad))
                self.stop(True)
                self.btnReset.setDisabled(False)
                if self.scoreToad >= 5:
                    self.reset()
                    self.bgResult.show()
                    self.bgResult.setPixmap(QtGui.QPixmap("../backgrounds/gameOverW.png"))
                return True
            if not tudo.__contains__("0"):
                self.btnReset.setDisabled(False)


        for i in tudo:
            if i.__contains__(0):
                return False
        return True

    def stop(self, cond):
        for i in self.btnP:
            i.setDisabled(cond)

    def reset(self):
        for i in self.btnP:
            i.setStyleSheet("background-color: rgb(0,0,0,0%); color: rgb(0,0,0,0%);")
            i.setText("0")
            self.stop(False)

    def quit(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = TicTacToe()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
