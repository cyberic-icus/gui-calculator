# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_ui4.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(425, 320)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Output = QtWidgets.QTextBrowser(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(10, 10, 401, 41))
        self.Output.setObjectName("Output")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 401, 170))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Four = QtWidgets.QPushButton(self.layoutWidget)
        self.Four.setStyleSheet("")
        self.Four.setObjectName("Four")
        self.gridLayout.addWidget(self.Four, 0, 1, 1, 1)
        self.One = QtWidgets.QPushButton(self.layoutWidget)
        self.One.setStyleSheet("")
        self.One.setObjectName("One")
        self.gridLayout.addWidget(self.One, 0, 0, 1, 1)
        self.Sin = QtWidgets.QPushButton(self.layoutWidget)
        self.Sin.setStyleSheet("")
        self.Sin.setObjectName("Sin")
        self.gridLayout.addWidget(self.Sin, 0, 4, 1, 1)
        self.Plus = QtWidgets.QPushButton(self.layoutWidget)
        self.Plus.setStyleSheet("")
        self.Plus.setObjectName("Plus")
        self.gridLayout.addWidget(self.Plus, 0, 3, 1, 1)
        self.Two = QtWidgets.QPushButton(self.layoutWidget)
        self.Two.setStyleSheet("")
        self.Two.setObjectName("Two")
        self.gridLayout.addWidget(self.Two, 1, 0, 1, 1)
        self.Five = QtWidgets.QPushButton(self.layoutWidget)
        self.Five.setStyleSheet("")
        self.Five.setObjectName("Five")
        self.gridLayout.addWidget(self.Five, 1, 1, 1, 1)
        self.Eight = QtWidgets.QPushButton(self.layoutWidget)
        self.Eight.setStyleSheet("")
        self.Eight.setObjectName("Eight")
        self.gridLayout.addWidget(self.Eight, 1, 2, 1, 1)
        self.Minus = QtWidgets.QPushButton(self.layoutWidget)
        self.Minus.setStyleSheet("")
        self.Minus.setObjectName("Minus")
        self.gridLayout.addWidget(self.Minus, 1, 3, 1, 1)
        self.Cos = QtWidgets.QPushButton(self.layoutWidget)
        self.Cos.setStyleSheet("")
        self.Cos.setObjectName("Cos")
        self.gridLayout.addWidget(self.Cos, 1, 4, 1, 1)
        self.Three = QtWidgets.QPushButton(self.layoutWidget)
        self.Three.setStyleSheet("")
        self.Three.setObjectName("Three")
        self.gridLayout.addWidget(self.Three, 2, 0, 1, 1)
        self.Six = QtWidgets.QPushButton(self.layoutWidget)
        self.Six.setStyleSheet("")
        self.Six.setObjectName("Six")
        self.gridLayout.addWidget(self.Six, 2, 1, 1, 1)
        self.Nine = QtWidgets.QPushButton(self.layoutWidget)
        self.Nine.setStyleSheet("")
        self.Nine.setObjectName("Nine")
        self.gridLayout.addWidget(self.Nine, 2, 2, 1, 1)
        self.Mul = QtWidgets.QPushButton(self.layoutWidget)
        self.Mul.setStyleSheet("")
        self.Mul.setObjectName("Mul")
        self.gridLayout.addWidget(self.Mul, 2, 3, 1, 1)
        self.Tg = QtWidgets.QPushButton(self.layoutWidget)
        self.Tg.setStyleSheet("")
        self.Tg.setObjectName("Tg")
        self.gridLayout.addWidget(self.Tg, 2, 4, 1, 1)
        self.Zero = QtWidgets.QPushButton(self.layoutWidget)
        self.Zero.setStyleSheet("")
        self.Zero.setObjectName("Zero")
        self.gridLayout.addWidget(self.Zero, 3, 0, 1, 2)
        self.Dot = QtWidgets.QPushButton(self.layoutWidget)
        self.Dot.setStyleSheet("")
        self.Dot.setObjectName("Dot")
        self.gridLayout.addWidget(self.Dot, 3, 2, 1, 1)
        self.Div = QtWidgets.QPushButton(self.layoutWidget)
        self.Div.setStyleSheet("")
        self.Div.setObjectName("Div")
        self.gridLayout.addWidget(self.Div, 3, 3, 1, 1)
        self.Ctg = QtWidgets.QPushButton(self.layoutWidget)
        self.Ctg.setStyleSheet("")
        self.Ctg.setObjectName("Ctg")
        self.gridLayout.addWidget(self.Ctg, 3, 4, 1, 1)
        self.Equals = QtWidgets.QPushButton(self.layoutWidget)
        self.Equals.setStyleSheet("")
        self.Equals.setObjectName("Equals")
        self.gridLayout.addWidget(self.Equals, 4, 0, 1, 2)
        self.LeftBracet = QtWidgets.QPushButton(self.layoutWidget)
        self.LeftBracet.setStyleSheet("")
        self.LeftBracet.setObjectName("LeftBracet")
        self.gridLayout.addWidget(self.LeftBracet, 4, 2, 1, 1)
        self.RightBracet = QtWidgets.QPushButton(self.layoutWidget)
        self.RightBracet.setStyleSheet("")
        self.RightBracet.setObjectName("RightBracet")
        self.gridLayout.addWidget(self.RightBracet, 4, 3, 1, 1)
        self.Sqrt = QtWidgets.QPushButton(self.layoutWidget)
        self.Sqrt.setStyleSheet("")
        self.Sqrt.setObjectName("Sqrt")
        self.gridLayout.addWidget(self.Sqrt, 4, 4, 1, 1)
        self.Seven = QtWidgets.QPushButton(self.layoutWidget)
        self.Seven.setStyleSheet("")
        self.Seven.setObjectName("Seven")
        self.gridLayout.addWidget(self.Seven, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 60, 131, 41))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 77, 54))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Clear = QtWidgets.QPushButton(self.widget)
        self.Clear.setObjectName("Clear")
        self.verticalLayout.addWidget(self.Clear)
        self.Result = QtWidgets.QPushButton(self.widget)
        self.Result.setObjectName("Result")
        self.verticalLayout.addWidget(self.Result)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.Four.setText(_translate("mainWindow", "4"))
        self.One.setText(_translate("mainWindow", "1"))
        self.Sin.setText(_translate("mainWindow", "sin"))
        self.Plus.setText(_translate("mainWindow", "+"))
        self.Two.setText(_translate("mainWindow", "2"))
        self.Five.setText(_translate("mainWindow", "5"))
        self.Eight.setText(_translate("mainWindow", "8"))
        self.Minus.setText(_translate("mainWindow", "-"))
        self.Cos.setText(_translate("mainWindow", "cos"))
        self.Three.setText(_translate("mainWindow", "3"))
        self.Six.setText(_translate("mainWindow", "6"))
        self.Nine.setText(_translate("mainWindow", "9"))
        self.Mul.setText(_translate("mainWindow", "*"))
        self.Tg.setText(_translate("mainWindow", "tg"))
        self.Zero.setText(_translate("mainWindow", "0"))
        self.Dot.setText(_translate("mainWindow", "."))
        self.Div.setText(_translate("mainWindow", "/"))
        self.Ctg.setText(_translate("mainWindow", "ctg"))
        self.Equals.setText(_translate("mainWindow", "="))
        self.LeftBracet.setText(_translate("mainWindow", "("))
        self.RightBracet.setText(_translate("mainWindow", ")"))
        self.Sqrt.setText(_translate("mainWindow", "sqrt"))
        self.Seven.setText(_translate("mainWindow", "7"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p>Made by <a href=\"https://github.com/cyberic-icus\"><span style=\" font-size:14px; font-weight:600; color:#000000; background-color:#f1f8ff;\">cyberic-icus</span></a></p></body></html>"))
        self.Clear.setText(_translate("mainWindow", "Clear"))
        self.Result.setText(_translate("mainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
