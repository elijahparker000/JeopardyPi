# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CloseWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase


class Ui_CloseWindow(object):
    def setupUi(self, CloseWindow):
        CloseWindow.setObjectName("CloseWindow")
        CloseWindow.resize(1824, 600)
        CloseWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(CloseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PS_DecoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PS_DecoLabel.setGeometry(QtCore.QRect(20, 540, 984, 60))
        self.PS_DecoLabel.setStyleSheet("background-color: #060CE9;")
        self.PS_DecoLabel.setText("")
        self.PS_DecoLabel.setObjectName("PS_DecoLabel")
        self.PS_P1Name = QtWidgets.QLabel(self.centralwidget)
        self.PS_P1Name.setGeometry(QtCore.QRect(59, 545, 150, 25))

        QFontDatabase.addApplicationFont("Fonts/Swiss 911 Compressed Regular.otf")
        QFontDatabase.addApplicationFont("Fonts/JeopardyPi/Korinna-Regular.otf")
        QFontDatabase.addApplicationFont("Fonts/Univers 75 Black Regular.otf")

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PS_P1Name.setFont(font)
        self.PS_P1Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P1Name.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P1Name.setObjectName("PS_P1Name")
        self.PS_P1Money = QtWidgets.QLabel(self.centralwidget)
        self.PS_P1Money.setGeometry(QtCore.QRect(59, 570, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PS_P1Money.setFont(font)
        self.PS_P1Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P1Money.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P1Money.setObjectName("PS_P1Money")
        self.PS_P2Name = QtWidgets.QLabel(self.centralwidget)
        self.PS_P2Name.setGeometry(QtCore.QRect(248, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PS_P2Name.setFont(font)
        self.PS_P2Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P2Name.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P2Name.setObjectName("PS_P2Name")
        self.PS_P3Name = QtWidgets.QLabel(self.centralwidget)
        self.PS_P3Name.setGeometry(QtCore.QRect(437, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PS_P3Name.setFont(font)
        self.PS_P3Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P3Name.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P3Name.setObjectName("PS_P3Name")
        self.PS_P4Name = QtWidgets.QLabel(self.centralwidget)
        self.PS_P4Name.setGeometry(QtCore.QRect(626, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PS_P4Name.setFont(font)
        self.PS_P4Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P4Name.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P4Name.setObjectName("PS_P4Name")
        self.PS_P5Name = QtWidgets.QLabel(self.centralwidget)
        self.PS_P5Name.setGeometry(QtCore.QRect(815, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PS_P5Name.setFont(font)
        self.PS_P5Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P5Name.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P5Name.setObjectName("PS_P5Name")
        self.PS_P2Money = QtWidgets.QLabel(self.centralwidget)
        self.PS_P2Money.setGeometry(QtCore.QRect(248, 570, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PS_P2Money.setFont(font)
        self.PS_P2Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P2Money.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P2Money.setObjectName("PS_P2Money")
        self.PS_P3Money = QtWidgets.QLabel(self.centralwidget)
        self.PS_P3Money.setGeometry(QtCore.QRect(437, 570, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PS_P3Money.setFont(font)
        self.PS_P3Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P3Money.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P3Money.setObjectName("PS_P3Money")
        self.PS_P4Money = QtWidgets.QLabel(self.centralwidget)
        self.PS_P4Money.setGeometry(QtCore.QRect(626, 570, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PS_P4Money.setFont(font)
        self.PS_P4Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P4Money.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P4Money.setObjectName("PS_P4Money")
        self.PS_P5Money = QtWidgets.QLabel(self.centralwidget)
        self.PS_P5Money.setGeometry(QtCore.QRect(815, 570, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PS_P5Money.setFont(font)
        self.PS_P5Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_P5Money.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_P5Money.setObjectName("PS_P5Money")
        self.AS_P5Name = QtWidgets.QLabel(self.centralwidget)
        self.AS_P5Name.setGeometry(QtCore.QRect(1029, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AS_P5Name.setFont(font)
        self.AS_P5Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P5Name.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P5Name.setObjectName("AS_P5Name")
        self.AS_DecoLabel = QtWidgets.QLabel(self.centralwidget)
        self.AS_DecoLabel.setGeometry(QtCore.QRect(1024, 420, 800, 60))
        self.AS_DecoLabel.setStyleSheet("background-color: #060CE9;")
        self.AS_DecoLabel.setText("")
        self.AS_DecoLabel.setObjectName("AS_DecoLabel")
        self.AS_P4Name = QtWidgets.QLabel(self.centralwidget)
        self.AS_P4Name.setGeometry(QtCore.QRect(1189, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AS_P4Name.setFont(font)
        self.AS_P4Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P4Name.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P4Name.setObjectName("AS_P4Name")
        self.AS_P3Name = QtWidgets.QLabel(self.centralwidget)
        self.AS_P3Name.setGeometry(QtCore.QRect(1349, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AS_P3Name.setFont(font)
        self.AS_P3Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P3Name.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P3Name.setObjectName("AS_P3Name")
        self.AS_P2Name = QtWidgets.QLabel(self.centralwidget)
        self.AS_P2Name.setGeometry(QtCore.QRect(1509, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AS_P2Name.setFont(font)
        self.AS_P2Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P2Name.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P2Name.setObjectName("AS_P2Name")
        self.AS_P1Name = QtWidgets.QLabel(self.centralwidget)
        self.AS_P1Name.setGeometry(QtCore.QRect(1669, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AS_P1Name.setFont(font)
        self.AS_P1Name.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P1Name.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P1Name.setObjectName("AS_P1Name")
        self.AS_P5Money = QtWidgets.QLabel(self.centralwidget)
        self.AS_P5Money.setGeometry(QtCore.QRect(1029, 450, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AS_P5Money.setFont(font)
        self.AS_P5Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P5Money.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P5Money.setObjectName("AS_P5Money")
        self.AS_P4Money = QtWidgets.QLabel(self.centralwidget)
        self.AS_P4Money.setGeometry(QtCore.QRect(1189, 450, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AS_P4Money.setFont(font)
        self.AS_P4Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P4Money.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P4Money.setObjectName("AS_P4Money")
        self.AS_P3Money = QtWidgets.QLabel(self.centralwidget)
        self.AS_P3Money.setGeometry(QtCore.QRect(1349, 450, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AS_P3Money.setFont(font)
        self.AS_P3Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P3Money.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P3Money.setObjectName("AS_P3Money")
        self.AS_P2Money = QtWidgets.QLabel(self.centralwidget)
        self.AS_P2Money.setGeometry(QtCore.QRect(1509, 450, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AS_P2Money.setFont(font)
        self.AS_P2Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P2Money.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P2Money.setObjectName("AS_P2Money")
        self.AS_P1Money = QtWidgets.QLabel(self.centralwidget)
        self.AS_P1Money.setGeometry(QtCore.QRect(1669, 450, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Univers 75 Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AS_P1Money.setFont(font)
        self.AS_P1Money.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.AS_P1Money.setAlignment(QtCore.Qt.AlignCenter)
        self.AS_P1Money.setObjectName("AS_P1Money")
        self.AS_DecoLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.AS_DecoLabel2.setGeometry(QtCore.QRect(1024, 290, 801, 121))
        self.AS_DecoLabel2.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.AS_DecoLabel2.setText("")
        self.AS_DecoLabel2.setObjectName("AS_DecoLabel2")
        self.PS_DecoLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.PS_DecoLabel2.setGeometry(QtCore.QRect(20, 0, 984, 524))
        self.PS_DecoLabel2.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.PS_DecoLabel2.setText("")
        self.PS_DecoLabel2.setObjectName("PS_DecoLabel2")
        self.PS_ClueLabel = QtWidgets.QLabel(self.centralwidget)
        self.PS_ClueLabel.setGeometry(QtCore.QRect(112, 80, 800, 431))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna Bold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.PS_ClueLabel.setFont(font)
        self.PS_ClueLabel.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.PS_ClueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PS_ClueLabel.setWordWrap(True)
        self.PS_ClueLabel.setObjectName("PS_ClueLabel")
        self.ReponseLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReponseLabel.setGeometry(QtCore.QRect(1024, 301, 800, 101))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ReponseLabel.setFont(font)
        self.ReponseLabel.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.ReponseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ReponseLabel.setWordWrap(True)
        self.ReponseLabel.setObjectName("ReponseLabel")
        self.closeJButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeJButton.setGeometry(QtCore.QRect(1034, 10, 380, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.closeJButton.setFont(font)
        self.closeJButton.setStyleSheet("QPushButton { background-color: #060CE9; border: 0px; color: #FFFFFF;}")
        self.closeJButton.setObjectName("closeJButton")
        self.shutdownButton = QtWidgets.QPushButton(self.centralwidget)
        self.shutdownButton.setGeometry(QtCore.QRect(1434, 10, 380, 131))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.shutdownButton.setFont(font)
        self.shutdownButton.setStyleSheet("QPushButton { background-color: #060CE9; border: 0px; color: #FFFFFF;}")
        self.shutdownButton.setObjectName("shutdownButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(1034, 160, 780, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton { background-color: #060CE9; border: 0px; color: #FFFFFF;}")
        self.cancelButton.setObjectName("cancelButton")
        self.shutdownButton.raise_()
        self.AS_DecoLabel2.raise_()
        self.closeJButton.raise_()
        self.PS_DecoLabel2.raise_()
        self.AS_DecoLabel.raise_()
        self.PS_DecoLabel.raise_()
        self.PS_P1Name.raise_()
        self.PS_P1Money.raise_()
        self.PS_P2Name.raise_()
        self.PS_P3Name.raise_()
        self.PS_P4Name.raise_()
        self.PS_P5Name.raise_()
        self.PS_P2Money.raise_()
        self.PS_P3Money.raise_()
        self.PS_P4Money.raise_()
        self.PS_P5Money.raise_()
        self.AS_P5Name.raise_()
        self.AS_P4Name.raise_()
        self.AS_P3Name.raise_()
        self.AS_P2Name.raise_()
        self.AS_P1Name.raise_()
        self.AS_P5Money.raise_()
        self.AS_P4Money.raise_()
        self.AS_P3Money.raise_()
        self.AS_P2Money.raise_()
        self.AS_P1Money.raise_()
        self.PS_ClueLabel.raise_()
        self.ReponseLabel.raise_()
        self.cancelButton.raise_()
        CloseWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CloseWindow)
        QtCore.QMetaObject.connectSlotsByName(CloseWindow)

    def retranslateUi(self, CloseWindow):
        _translate = QtCore.QCoreApplication.translate
        CloseWindow.setWindowTitle(_translate("CloseWindow", "MainWindow"))
        self.PS_P1Name.setText(_translate("CloseWindow", "Player1"))
        self.PS_P1Money.setText(_translate("CloseWindow", "$0"))
        self.PS_P2Name.setText(_translate("CloseWindow", "Player2"))
        self.PS_P3Name.setText(_translate("CloseWindow", "Player3"))
        self.PS_P4Name.setText(_translate("CloseWindow", "Player4"))
        self.PS_P5Name.setText(_translate("CloseWindow", "Player5"))
        self.PS_P2Money.setText(_translate("CloseWindow", "$0"))
        self.PS_P3Money.setText(_translate("CloseWindow", "$0"))
        self.PS_P4Money.setText(_translate("CloseWindow", "$0"))
        self.PS_P5Money.setText(_translate("CloseWindow", "$0"))
        self.AS_P5Name.setText(_translate("CloseWindow", "Player5"))
        self.AS_P4Name.setText(_translate("CloseWindow", "Player4"))
        self.AS_P3Name.setText(_translate("CloseWindow", "Player3"))
        self.AS_P2Name.setText(_translate("CloseWindow", "Player2"))
        self.AS_P1Name.setText(_translate("CloseWindow", "Player1"))
        self.AS_P5Money.setText(_translate("CloseWindow", "$0"))
        self.AS_P4Money.setText(_translate("CloseWindow", "$0"))
        self.AS_P3Money.setText(_translate("CloseWindow", "$0"))
        self.AS_P2Money.setText(_translate("CloseWindow", "$0"))
        self.AS_P1Money.setText(_translate("CloseWindow", "$0"))
        self.PS_ClueLabel.setText(_translate("CloseWindow", "Waiting on input from Alex"))
        self.ReponseLabel.setText(_translate("CloseWindow", "Would you like to close the game or shutdown? Note: a mouse is required to navigate after closing the game. Press cancel to return to the game. "))
        self.closeJButton.setText(_translate("CloseWindow", "Close Jeopardy"))
        self.shutdownButton.setText(_translate("CloseWindow", "Shutdown"))
        self.cancelButton.setText(_translate("CloseWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CloseWindow = QtWidgets.QMainWindow()
    ui = Ui_CloseWindow()
    ui.setupUi(CloseWindow)
    CloseWindow.show()
    sys.exit(app.exec_())
