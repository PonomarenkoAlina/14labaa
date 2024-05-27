import sys
import warnings
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self): 
        super(CurrencyConv, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.pushButton.clicked.connect(self.converter) #  кнопка converter

    def init_UI(self):
        self.setWindowTitle('Конвертер валют')
        self.setWindowIcon(QIcon('png-klev.png'))

        
        self.ui.input_cur.setPlaceholderText('Из валюты')
        self.ui.input_cur.setAlignment(QtCore.Qt.AlignCenter)
        
        self.ui.input_sum.setPlaceholderText('Сколько')
        self.ui.input_sum.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.output_cur.setPlaceholderText('В валюту')
        self.ui.output_cur.setAlignment(QtCore.Qt.AlignCenter)
        
        self.ui.output_sum.setPlaceholderText('Итого')
        self.ui.output_sum.setAlignment(QtCore.Qt.AlignCenter)

    def converter(self):
        c = CurrencyConverter()
        input_cur = self.ui.input_cur.text()
        output_cur = self.ui.output_cur.text()

        try:  # преобраз введенную сумму в число
            input_sum = float(self.ui.input_sum.text())
        except ValueError:
            self.ui.output_sum.setText('Ошибка: ввод должен быть числом')
            return

        try:  # выполн конвертации валюты
            output_sum = round(c.convert(input_sum, '%s' % (input_cur), '%s' % (output_cur)), 2)
            self.ui.output_sum.setText(str(output_sum))
        except ValueError:
            self.ui.output_sum.setText('Ошибка: неверная валюта')


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
