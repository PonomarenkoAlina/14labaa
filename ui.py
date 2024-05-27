


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 270))
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 0, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.input_cur = QtWidgets.QLineEdit(self.centralwidget)
        self.input_cur.setGeometry(QtCore.QRect(50, 320, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.input_cur.setFont(font)
        self.input_cur.setStyleSheet("background-color : #22222e;\n"
"border : 2px solid #f66867;\n"
"border-radius : 30;\n"
"color : white;")
        self.input_cur.setObjectName("input_cur")
        self.input_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sum.setGeometry(QtCore.QRect(50, 390, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.input_sum.setFont(font)
        self.input_sum.setStyleSheet("background-color : #22222e;\n"
"border : 2px solid #f66867;\n"
"border-radius : 30;\n"
"color : white;")
        self.input_sum.setObjectName("input_sum")
        self.output_sum = QtWidgets.QLineEdit(self.centralwidget)
        self.output_sum.setGeometry(QtCore.QRect(50, 530, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.output_sum.setFont(font)
        self.output_sum.setStyleSheet("background-color : #22222e;\n"
"border : 2px solid #f66867;\n"
"border-radius : 30;\n"
"color : white;")
        self.output_sum.setObjectName("output_sum")
        self.output_cur = QtWidgets.QLineEdit(self.centralwidget)
        self.output_cur.setGeometry(QtCore.QRect(50, 460, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.output_cur.setFont(font)
        self.output_cur.setStyleSheet("background-color : #22222e;\n"
"border : 2px solid #f66867;\n"
"border-radius : 30;\n"
"color : white;")
        self.output_cur.setObjectName("output_cur")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 620, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#fb5b5d;\n"
"border-radius:30;\n"
"color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#fa4244;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Конвертер валют"))
        self.pushButton.setText(_translate("MainWindow", "Конвертация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
