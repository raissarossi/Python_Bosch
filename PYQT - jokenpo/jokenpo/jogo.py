import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui, uic, QtWidgets

class Window (QMainWindow):
	def __init__(self):
		super().__init__()
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300
		self.title = "Rock-Paper-Scissors"

		self.startScreen = QLabel(self)
		self.startScreen.setStyleSheet("QLabel {backgroud-image: url(backgroud.jpg)}")
		self.startScreen.resize(400, 300)
		self.startScreen.setText("WELLCOME TO\n\n\n\n\n\nJOKEMPO")
		self.startScreen.setStyleSheet("background-image:url(background.jpg) ;font:bold; font-size:30px; color:#000; padding-left: 80px; padding-top:30px")

		button1 = QPushButton('Start', self)
		button1.move(250, 260)  # padding left and padding top
		button1.resize(80, 30)  # width and height
		button1.setStyleSheet('QPushButton {background-color:#C167A6; font:bold; font-size:20px; color:#fff; border: 4px solid #000}; ')
		button1.clicked.connect(secondScreen(self))
		self.loadWindow()



		self.gameScreen = QLabel(self)
		self.gameScreen.setStyleSheet("QLabel {backgroud: #000)}")
		self.gameScreen.resize(400, 300)



	def loadWindow(self):
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.show()

	def sencondScreen(self):
		secScreen.show()
app = QtWidgets.QApplication([])
firstScreen = self.startScreen


	def startClick(self):
		print('oi')
		self.loadWindow2()


application = QApplication(sys.argv)
w = Window()
sys.exit(application.exec_())