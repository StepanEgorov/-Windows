from PyQt5 import QtCore, QtGui, QtWidgets
class first_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(first_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton = QtWidgets.QPushButton( self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(445, 373, 130, 35))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.setStyleSheet('.QWidget {background-image: url(1.jpg);}')
    def on_pushButton_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class second_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(second_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 383, 230, 20))
        self.lineEdit.setText("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_2.setGeometry(QtCore.QRect(500, 535, 175, 39))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.setStyleSheet('.QWidget {background-image: url(3.jpg);}')
    def on_pushButton_2_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class third_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(third_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_3.setGeometry(QtCore.QRect(740, 548, 75, 20))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
        self.setStyleSheet('.QWidget {background-image: url(4.jpg);}')
    def on_pushButton_3_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class fourth_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(fourth_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_4.setGeometry(QtCore.QRect(240, 315, 530, 120))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_4.clicked.connect(self.on_pushButton_4_clicked)
        self.setStyleSheet('.QWidget {background-image: url(5.jpg);}')
    def on_pushButton_4_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class fifth_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(fifth_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_5.setGeometry(QtCore.QRect(735, 549, 75, 20))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_5.clicked.connect(self.on_pushButton_5_clicked)
        self.setStyleSheet('.QWidget {background-image: url(6.jpg);}')
    def on_pushButton_5_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class sixth_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(sixth_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_6.setGeometry(QtCore.QRect(670, 549, 145, 20))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_6.clicked.connect(self.on_pushButton_6_clicked)
        self.setStyleSheet('.QWidget {background-image: url(7.jpg);}')
    def on_pushButton_6_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class seventh_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(seventh_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_7.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_7.clicked.connect(self.on_pushButton_7_clicked)
        self.setStyleSheet('.QWidget {background-image: url(8.jpg);}')
    def on_pushButton_7_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class eighth_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(eighth_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_8.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_8.clicked.connect(self.on_pushButton_8_clicked)
        self.setStyleSheet('.QWidget {background-image: url(9.jpg);}')
    def on_pushButton_8_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class nineth_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(nineth_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_9.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_9.clicked.connect(self.on_pushButton_9_clicked)
        self.setStyleSheet('.QWidget {background-image: url(10.jpg);}')
    def on_pushButton_9_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class tenth_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(tenth_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_10.clicked.connect(self.on_pushButton_10_clicked)
        self.setStyleSheet('.QWidget {background-image: url(11.jpg);}')
    def on_pushButton_10_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
class eleventh_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None, satellite=None):
        super(eleventh_window, self).__init__(parent)
        self.w_sat = satellite
        self.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.pushButton_11.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Установка Windows")
        self.pushButton_11.clicked.connect(self.on_pushButton_11_clicked)
        self.setStyleSheet('.QWidget {background-image: url(12.jpg);}')
    def on_pushButton_11_clicked(self, val):
        if self.w_sat is not None:
            self.w_sat.show()
            self.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fwin = first_window()
    elwin = eleventh_window()
    tewin = tenth_window(
          satellite=elwin
    )
    nwin = nineth_window(
         satellite=tewin
    )
    ewin = eighth_window(
         satellite=nwin
    )
    sewin = seventh_window(
          satellite=ewin
    )
    sixwin = sixth_window(
           satellite=sewin
    )
    fiwin = fifth_window(
          satellite=sixwin
    )
    fowin = fourth_window(
         satellite=fiwin
         )
    twin = third_window(
        satellite=fowin
        )
    fwin.move(0, 0)
    fwin.show()
    swin = second_window(
        satellite=twin
        )
    swin.move(0, 0)
    twin.move(0, 0)
    fowin.move(0, 0)
    fiwin.move(0, 0)
    sixwin.move(0, 0)
    sewin.move(0, 0)
    ewin.move(0, 0)
    nwin.move(0, 0)
    tewin.move(0, 0)
    elwin.move(0, 0)
    fwin.w_sat = swin
    app.exec_()