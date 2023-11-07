import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from MainWindowUi import Ui_MainWindow

# Для сборки ui файла команда: pyuic5 <>.ui -o <>.py
# Библиотека pip install pyqt5

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.lineEdit.setEnabled(False)
        self.line = str()
        self.operation = None
        self.prev_number = None
        self.__add_callbacks()

    def __add_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.__add_digit_to_line(self.ui.pushButton_9.text()))
        self.ui.pushButton_10.clicked.connect(lambda: self.__make_operation(self.ui.pushButton_10.text()))
        self.ui.pushButton_11.clicked.connect(lambda: self.__make_operation(self.ui.pushButton_11.text()))
        self.ui.pushButton_12.clicked.connect(self.__calculate)

    def __add_digit_to_line(self, value):
        self.line += value
        self.ui.lineEdit.setText(self.line)

    def __make_operation(self, value):
        self.operation = value
        self.prev_number = int(self.line)
        self.line = str()
        self.ui.lineEdit.clear()

    def __calculate(self):
        match self.operation:
            case '+':
                self.line = str(self.prev_number + int(self.line))
                self.ui.lineEdit.setText(self.line)
            case '-':
                self.line = str(self.prev_number - int(self.line))
                self.ui.lineEdit.setText(self.line)
            case _:
                print('No operation')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    app.exec()
