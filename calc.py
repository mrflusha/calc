import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QDialog):
	"""docstring for App"""
	def __init__(self):
		super().__init__()
		self.title = "Calc"
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)

		self.createGridLayout()
		windowLayout = QVBoxLayout()
		windowLayout.addWidget(self.horizontalGroupBox)
		self.setLayout(windowLayout)

		self.show()

	def createGridLayout(self):
		self.horizontalGroupBox = QGroupBox("")
		layout = QGridLayout()
		layout.setColumnStretch(0,1)
		layout.setColumnStretch(4,3)
		button_one = QPushButton("1")
		button_two = QPushButton("2")
		button_three = QPushButton("3")
		button_four = QPushButton("4")
		button_five = QPushButton("5")
		button_six = QPushButton("6")
		button_seven = QPushButton("7")
		button_eight = QPushButton("8")
		button_nine = QPushButton("9")
		button_null = QPushButton("0")
		button_dot = QPushButton(".")
		button_close = QPushButton("c")
		button_plus = QPushButton("+")
		button_minus = QPushButton("-")
		button_div = QPushButton("/")
		button_op = QPushButton("*")
		button_sum = QPushButton("=")
		input_one = QLineEdit()
		input_two = QLineEdit()

		layout.addWidget(input_one,0,0)
		layout.addWidget(QLabel(""),0,1)
		layout.addWidget(input_two,0,2)
		
		layout.addWidget(button_sum,0,3)
		layout.addWidget(button_one,1,0)
		layout.addWidget(button_two,1,1)
		layout.addWidget(button_three,1,2)
		layout.addWidget(button_op,1,3)
		layout.addWidget(button_four,2,0)
		layout.addWidget(button_five,2,1)
		layout.addWidget(button_six,2,2)
		layout.addWidget(button_div,2,3)
		layout.addWidget(button_seven,3,0)
		layout.addWidget(button_eight,3,1)
		layout.addWidget(button_nine,3,2)
		layout.addWidget(button_minus,3,3)
		layout.addWidget(button_null,4,1)
		layout.addWidget(button_close,4,0)
		layout.addWidget(button_dot,4,2)
		layout.addWidget(button_plus,4,3)


		self.horizontalGroupBox.setLayout(layout)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
		