from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc

class Ui_JeopardyBoard(QtWidgets.QWidget):
    buttonClicked = QtCore.pyqtSignal(str)  # Custom signal to emit the button name

    def setupUi(self, JeopardyBoard):
        JeopardyBoard.setObjectName("JeopardyBoard")
        JeopardyBoard.resize(4095, 3000)
        JeopardyBoard.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(JeopardyBoard)
        self.centralwidget.setObjectName("centralwidget")

        self.cat1clue1 = QtWidgets.QPushButton(self.centralwidget)
        self.cat1clue1.setGeometry(QtCore.QRect(20, 20, 860, 480))
        self.cat1clue1.setStyleSheet("background-image: url(:/images/png/dollar_200.png);")
        self.cat1clue1.setText("")
        self.cat1clue1.setObjectName("cat1clue1")

        self.cat1clue2 = QtWidgets.QPushButton(self.centralwidget)
        self.cat1clue2.setGeometry(QtCore.QRect(20, 500, 860, 480))
        self.cat1clue2.setStyleSheet("background-image: url(:/images/png/dollar_400.png);")
        self.cat1clue2.setText("")
        self.cat1clue2.setObjectName("cat1clue2")

        self.cat1clue3 = QtWidgets.QPushButton(self.centralwidget)
        self.cat1clue3.setGeometry(QtCore.QRect(20, 980, 860, 480))
        self.cat1clue3.setStyleSheet("background-image: url(:/images/png/dollar_600.png);")
        self.cat1clue3.setText("")
        self.cat1clue3.setObjectName("cat1clue3")

        self.cat1clue4 = QtWidgets.QPushButton(self.centralwidget)
        self.cat1clue4.setGeometry(QtCore.QRect(20, 1460, 860, 480))
        self.cat1clue4.setStyleSheet("background-image: url(:/images/png/dollar_800.png);")
        self.cat1clue4.setText("")
        self.cat1clue4.setObjectName("cat1clue4")

        self.cat1clue5 = QtWidgets.QPushButton(self.centralwidget)
        self.cat1clue5.setGeometry(QtCore.QRect(20, 1940, 860, 480))
        self.cat1clue5.setStyleSheet("background-image: url(:/images/png/dollar_1000.png);")
        self.cat1clue5.setText("")
        self.cat1clue5.setObjectName("cat1clue5")

        JeopardyBoard.setCentralWidget(self.centralwidget)

        self.retranslateUi(JeopardyBoard)
        QtCore.QMetaObject.connectSlotsByName(JeopardyBoard)

        self.connect_signals()

    def retranslateUi(self, JeopardyBoard):
        _translate = QtCore.QCoreApplication.translate
        JeopardyBoard.setWindowTitle(_translate("JeopardyBoard", "JeopardyBoard"))

    def connect_signals(self):
        self.cat1clue1.clicked.connect(lambda: self.emit_button_name(self.cat1clue1))
        self.cat1clue2.clicked.connect(lambda: self.emit_button_name(self.cat1clue2))
        self.cat1clue3.clicked.connect(lambda: self.emit_button_name(self.cat1clue3))
        self.cat1clue4.clicked.connect(lambda: self.emit_button_name(self.cat1clue4))
        self.cat1clue5.clicked.connect(lambda: self.emit_button_name(self.cat1clue5))

    def emit_button_name(self, button):
        self.buttonClicked.emit(button.objectName())  # Emit the custom signal with the button name
