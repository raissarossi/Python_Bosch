import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui

class Window (QMainWindow):
	def __init__(self):
		super().__init__()
		self.top = 100
		self.left = 100
		self.width = 800
		self.height = 600
		self.title = "Fist window"

		button1 = QPushButton('Button 1',self)
		button1.move(150, 200) #padding left and padding top
		button1.resize(150, 80) #width and height
		button1.setStyleSheet('QPushButton {background-color:#246B66; font:bold; font-size:20px; color:#fff}')
		button1.clicked.connect(self.button1Click)

		button2 = QPushButton('Button 1', self)
		button2.move(450, 200)  # padding left and padding top
		button2.resize(150, 80)  # width and height
		button2.setStyleSheet('QPushButton {background-color:#720043; font:bold; font-size:20px; color:#fff}')
		button2.clicked.connect(self.button2Click)

		self.label1 = QLabel(self)
		self.label1.setText("Choose a Button")
		self.label1.move(150,100)
		self.label1.setStyleSheet('QLabel {font:bold; font-size:20px}')
		self.label1.resize(250, 25)

		self.car = QLabel(self)
		self.car.move(50, 350)
		# self.car.setPixmap(QtGui.QPixmap('car.jpg'))
		self.car.resize(700, 250)

		self.loadWindow()

	def loadWindow(self):
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)
		self.show()

	def button1Click(self):
		print('The Button 1 was click')
		self.label1.setText('You pressed button 1')
		self.label1.setStyleSheet('QLabel {color:#246B66; font:bold; font-size:20px}')
		self.label1.resize(250, 25)
		self.car.setPixmap(QtGui.QPixmap('car.jpg'))

	def button2Click(self):
		print('The Button 2 was click')
		self.label1.setText('You pressed button 2')
		self.label1.setStyleSheet('QLabel {color:#720043; font:bold; font-size:20px}')
		self.label1.resize(250, 25)
		self.car.setPixmap(QtGui.QPixmap(''))

application = QApplication(sys.argv)
w = Window()
sys.exit(application.exec_())