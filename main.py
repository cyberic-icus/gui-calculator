from PyQt5 import QtWidgets
from ui import Ui_mainWindow
import main_functions

class ExampleApp(QtWidgets.QMainWindow, Ui_mainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.One.clicked.connect(self.one)
		self.Two.clicked.connect(self.two)
		self.Three.clicked.connect(self.three)
		self.Four.clicked.connect(self.four)
		self.Five.clicked.connect(self.five)
		self.Six.clicked.connect(self.six)
		self.Seven.clicked.connect(self.seven)
		self.Eight.clicked.connect(self.eight)
		self.Nine.clicked.connect(self.nine)
		self.Zero.clicked.connect(self.zero)

		self.Plus.clicked.connect(self.plus)
		self.Minus.clicked.connect(self.minus)
		self.Mul.clicked.connect(self.mul)
		self.Div.clicked.connect(self.div)

		self.Dot.clicked.connect(self.dot)
		self.LeftBracet.clicked.connect(self.leftbracet)
		self.RightBracet.clicked.connect(self.rightbracet)
		self.Sin.clicked.connect(self.sin)
		self.Cos.clicked.connect(self.cos)
		self.Tg.clicked.connect(self.tg)
		self.Ctg.clicked.connect(self.ctg)
		self.Sqrt.clicked.connect(self.sqrt)

		self.Result.clicked.connect(self.result)
		self.Clear.clicked.connect(self.clear)
		self.Equals.clicked.connect(self.calculate)

		self._exp = ''
		self._result = ''

	def zero(self):
		self._exp = self._exp +'0'
		self.Output.setText(self._exp)


	def one(self):
		self._exp = self._exp +'1'
		self.Output.setText(self._exp)


	def two(self):
		self._exp = self._exp +'2'
		self.Output.setText(self._exp)


	def three(self):
		self._exp = self._exp +'3'
		self.Output.setText(self._exp)


	def four(self):
		self._exp = self._exp +'4'
		self.Output.setText(self._exp)


	def five(self):
		self._exp = self._exp +'5'
		self.Output.setText(self._exp)


	def six(self):
		self._exp = self._exp +'6'
		self.Output.setText(self._exp)


	def seven(self):
		self._exp = self._exp +'7'
		self.Output.setText(self._exp)


	def eight(self):
		self._exp = self._exp +'8'
		self.Output.setText(self._exp)


	def nine(self):
		self._exp = self._exp +'9'
		self.Output.setText(self._exp)

	def plus(self):
		self._exp = self._exp +'+'
		self.Output.setText(self._exp)


	def minus(self):
		self._exp = self._exp +'-'
		self.Output.setText(self._exp)


	def mul(self):
		self._exp = self._exp +'*'
		self.Output.setText(self._exp)

	def div(self):
		self._exp = self._exp +'/'
		self.Output.setText(self._exp)

	def dot(self):
		self._exp = self._exp +'.'
		self.Output.setText(self._exp)

	def leftbracet(self):
		self._exp = self._exp +'('
		self.Output.setText(self._exp)

	def rightbracet(self):
		self._exp = self._exp +')'
		self.Output.setText(self._exp)	

	def sin(self):
		self._exp = self._exp +'sin'
		self.Output.setText(self._exp)

	def cos(self):
		self._exp = self._exp +'cos'
		self.Output.setText(self._exp)

	def tg(self):
		self._exp = self._exp +'tg'
		self.Output.setText(self._exp)

	def ctg(self):
		self._exp = self._exp +'ctg'
		self.Output.setText(self._exp)

	def sqrt(self):
		self._exp = self._exp +'sqrt'
		self.Output.setText(self._exp)

	def result(self):
		self._exp = self._exp +self._result
		self.Output.setText(self._exp)


	def clear(self):
		self._exp = ''
		self.Output.setText(self._exp)

	def calculate(self):
		result = main_functions.calculate(self._exp)
		self._result = str(result)
		self.Output.setText(f'{self._exp} = {result}')

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = ExampleApp()
	window.show()
	app.exec_()
