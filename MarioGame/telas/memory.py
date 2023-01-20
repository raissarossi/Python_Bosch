import random
import sys, os

import winsound
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel
from PyQt5 import uic, QtGui

class Memory(QWidget):
    def __init__(self):

        winsound.PlaySound("../songs/marioKart_Memory.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

        super(Memory, self).__init__()
        uic.loadUi("memory.ui", self)
        self.setWindowTitle("Memory Game")

        self.btns = []
        for x in range(0, 24):
            btn = self.findChild(QPushButton, "btn_"+str(x))
            self.btns.append(btn)
        # print(self.btns[0])
        self.lblBackground = self.findChild(QLabel, "lblBackground")
        self.lblPlayerPoints = [0, 0]
        self.lblPlayerPoints[0] = self.findChild(QLabel, "lblPlayer1Points")
        self.lblPlayerPoints[1] = self.findChild(QLabel, "lblPlayer2Points")
        self.lblTurn = self.findChild(QLabel, "lblTurn")
        self.lblp = [[0, 0, 0, 0], [0, 0, 0, 0]]

        # self.btnJoin = self.findChild(QPushButton, "btnSecondPlayer")

        self.btns[0].clicked.connect(lambda: self.num(0))
        self.btns[1].clicked.connect(lambda: self.num(1))
        self.btns[2].clicked.connect(lambda: self.num(2))
        self.btns[3].clicked.connect(lambda: self.num(3))
        self.btns[4].clicked.connect(lambda: self.num(4))
        self.btns[5].clicked.connect(lambda: self.num(5))
        self.btns[6].clicked.connect(lambda: self.num(6))
        self.btns[7].clicked.connect(lambda: self.num(7))
        self.btns[8].clicked.connect(lambda: self.num(8))
        self.btns[9].clicked.connect(lambda: self.num(9))
        self.btns[10].clicked.connect(lambda: self.num(10))
        self.btns[11].clicked.connect(lambda: self.num(11))
        self.btns[12].clicked.connect(lambda: self.num(12))
        self.btns[13].clicked.connect(lambda: self.num(13))
        self.btns[14].clicked.connect(lambda: self.num(14))
        self.btns[15].clicked.connect(lambda: self.num(15))
        self.btns[16].clicked.connect(lambda: self.num(16))
        self.btns[17].clicked.connect(lambda: self.num(17))
        self.btns[18].clicked.connect(lambda: self.num(18))
        self.btns[19].clicked.connect(lambda: self.num(19))
        self.btns[20].clicked.connect(lambda: self.num(20))
        self.btns[21].clicked.connect(lambda: self.num(21))
        self.btns[22].clicked.connect(lambda: self.num(22))
        self.btns[23].clicked.connect(lambda: self.num(23))

        self.vez = False
        self.pc = True
        self.num1 = -1
        self.num2 = -1

        self.setStyle1 = ""
        self.setStyle2 = ""

        self.player = 1

        self.sortear()

        self.show()

    def sortear(self):
        imgs = ["../elements/cube1.png", "../elements/cube2.png", "../elements/cube3.png", "../elements/cube4.png",
                "../elements/cube5.png", "../elements/cube6.png", "../elements/cube7.png", "../elements/cube8.png",
                "../elements/cube9.png", "../elements/cube10.png", "../elements/cube11.png", "../elements/cube12.png",
                "../elements/cube1.png", "../elements/cube2.png", "../elements/cube3.png", "../elements/cube4.png",
                "../elements/cube5.png", "../elements/cube6.png", "../elements/cube7.png", "../elements/cube8.png",
                "../elements/cube9.png", "../elements/cube10.png", "../elements/cube11.png", "../elements/cube12.png"]

        for i in self.btns:
            num = random.randint(0, (len(imgs)-1))
            i.setStyleSheet("border-image: url(../elements/cube.png)")
            i.setObjectName(f"border-image: url({imgs[num]})")
            imgs.remove(imgs[num])
        print(len(imgs))

    def num(self, num):
        print(num)
        print(self.btns[num].objectName())
        print(self.btns[num].styleSheet())

        style = self.btns[num].objectName()
        name = self.btns[num].styleSheet()
        self.btns[num].setObjectName(name)
        self.btns[num].setStyleSheet(style)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    memoria = Memory()
    app.exec()
