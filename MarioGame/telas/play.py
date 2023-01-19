from forca import Forca
from jokenpo import Jokenpo
from ticTacToe import TicTacToe
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_playWindow(object):
    def setupUi(self, playWindow):
        playWindow.setObjectName("playWindow")
        playWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(playWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.backgroundPlay = QtWidgets.QLabel(self.centralwidget)
        self.backgroundPlay.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.backgroundPlay.setText("")
        # self.backgroundPlay.setPixmap(QtGui.QPixmap("../backgrounds/capaInicial.png"))
        self.gif = QMovie("../elements/SuperMario.gif")
        self.gif = QMovie("../elements/SuperMario.gif")
        self.backgroundPlay.setMovie(self.gif)
        self.gif.start()
        self.backgroundPlay.setObjectName("bgPlay")

        
        self.btnPlay = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlay.setGeometry(QtCore.QRect(70, 110, 151, 501))
        self.btnPlay.setStyleSheet("background-color: rgb(0,0,0,0%)")
        self.btnPlay.setText("")
        self.btnPlay.setObjectName("btnPlay")
        self.btnPlay.clicked.connect(self.startPlay)

        self.btnMemory = QtWidgets.QPushButton(self.centralwidget)
        self.btnMemory.setGeometry(QtCore.QRect(360, 110, 121, 111))
        self.btnMemory.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnMemory.setText("")
        self.btnMemory.setObjectName("btnMemory")
        self.btnMemory.setDisabled(True)
        self.btnMemory.clicked.connect(self.openMemory)

        self.btnForca = QtWidgets.QPushButton(self.centralwidget)
        self.btnForca.setGeometry(QtCore.QRect(560, 110, 121, 111))
        self.btnForca.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnForca.setText("")
        self.btnForca.setObjectName("btnForca")
        self.btnForca.setDisabled(True)
        self.btnForca.clicked.connect(self.openForca)

        self.btnTicTacToe = QtWidgets.QPushButton(self.centralwidget)
        self.btnTicTacToe.setGeometry(QtCore.QRect(780, 110, 141, 111))
        self.btnTicTacToe.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnTicTacToe.setText("")
        self.btnTicTacToe.setObjectName("btnTicTacToe")
        self.btnTicTacToe.setDisabled(True)
        self.btnTicTacToe.clicked.connect(self.openTicTacToe)


        self.btnJokenpo = QtWidgets.QPushButton(self.centralwidget)
        self.btnJokenpo.setGeometry(QtCore.QRect(1040, 110, 171, 111))
        self.btnJokenpo.setStyleSheet("background-color: rgb(0,0,0,0%);")
        self.btnJokenpo.setText("")
        self.btnJokenpo.setObjectName("btnJokenpo")
        self.btnJokenpo.setDisabled(True)
        self.btnJokenpo.clicked.connect(self.openJokenpo)

        playWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(playWindow)
        QtCore.QMetaObject.connectSlotsByName(playWindow)

    def retranslateUi(self, playWindow):
        _translate = QtCore.QCoreApplication.translate
        playWindow.setWindowTitle(_translate("playWindow", "MainWindow"))

    def startPlay(self):
        print("okk")
        self.backgroundPlay.setPixmap(QtGui.QPixmap("../backgrounds/menuGames.png"))
        self.btnPlay.setDisabled(True)
        self.btnMemory.setDisabled(False)
        self.btnForca.setDisabled(False)
        self.btnJokenpo.setDisabled(False)
        self.btnTicTacToe.setDisabled(False)

    def openMemory(self):
        print("Memory")

    def openForca(self):
        print("Forca")
        self.window  = QtWidgets.QWidget()
        self.ui = Forca()
        self.ui.setupUi(self.window)
        self.window.show()

    def openTicTacToe(self):
        print("TicTacToe")
        self.window  = QtWidgets.QWidget()
        self.ui = TicTacToe()
        self.ui.setupUi(self.window)
        self.window.show()

    def openJokenpo(self):
        print("Jokenpo")
        self.window  = QtWidgets.QWidget()
        self.ui = Jokenpo()
        self.ui.setupUi(self.window)
        self.window.show()


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    playWindow = QtWidgets.QMainWindow()
    ui = Ui_playWindow()
    ui.setupUi(playWindow)
    playWindow.show()
    sys.exit(app.exec_())


