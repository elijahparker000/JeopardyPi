# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#TODO:for some reason the bold isn't working or at least the numbers on the buttons don't look right.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1824, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(26, 16, 157, 78))

        QFontDatabase.addApplicationFont("C:/Users/elija/OneDrive/Desktop/PythonScripts/JeopardyProjectRepo/JeopardyPi/Swiss 911 Compressed Regular.otf")
        QFontDatabase.addApplicationFont("C:/Users/elija/OneDrive/Desktop/PythonScripts/JeopardyProjectRepo/JeopardyPi/Korinna-Regular.otf")

        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1004, 0, 20, 600))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 20, 600))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 540, 984, 60))
        self.label_4.setStyleSheet("background-color: #060CE9;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(59, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(59, 570, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(248, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(437, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(626, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(815, 545, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(248, 570, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(437, 570, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(626, 570, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(815, 570, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(26, 110, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(189, 110, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(352, 110, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(515, 110, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(678, 110, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(841, 110, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(26, 194, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(26, 278, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(26, 362, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(26, 446, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(189, 194, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(678, 194, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(515, 194, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(352, 194, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(189, 278, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(352, 278, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(515, 278, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.testbutton600 = QtWidgets.QPushButton(self.centralwidget)
        self.testbutton600.setGeometry(QtCore.QRect(841, 278, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.testbutton600.setFont(font)
        self.testbutton600.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.testbutton600.setObjectName("testbutton600")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(678, 278, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(189, 362, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(678, 362, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(515, 362, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(352, 362, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(841, 362, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(515, 446, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(678, 446, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_32.setObjectName("pushButton_32")
        self.testbutton2000 = QtWidgets.QPushButton(self.centralwidget)
        self.testbutton2000.setGeometry(QtCore.QRect(841, 446, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.testbutton2000.setFont(font)
        self.testbutton2000.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.testbutton2000.setObjectName("testbutton2000")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(352, 446, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(189, 446, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(189, 16, 157, 78))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(352, 16, 157, 78))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(515, 16, 157, 78))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(678, 16, 157, 78))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(841, 16, 157, 78))
        font = QtGui.QFont()
        font.setFamily("ITC Korinna")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(841, 194, 157, 78))
        font = QtGui.QFont()
        font.setFamily("Swiss 911 Compressed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("background-color: #060CE9;\n"
"color: #d69f4c;")
        self.pushButton_36.setObjectName("pushButton_36")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1024, 0, 800, 480))
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(1764, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1029, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1024, 420, 800, 60))
        self.label_17.setStyleSheet("background-color: #060CE9;")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1189, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1349, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1509, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1669, 425, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1029, 450, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1189, 450, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(1349, 450, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(1509, 450, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(1669, 450, 150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: #060CE9;\n"
"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label.raise_()
        self.label_17.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        self.testbutton600.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.testbutton2000.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_36.raise_()
        self.pushButton_24.raise_()
        self.label_15.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Cat1"))
        self.label_5.setText(_translate("MainWindow", "Player1"))
        self.label_6.setText(_translate("MainWindow", "$0"))
        self.label_7.setText(_translate("MainWindow", "Player2"))
        self.label_8.setText(_translate("MainWindow", "Player3"))
        self.label_9.setText(_translate("MainWindow", "Player4"))
        self.label_10.setText(_translate("MainWindow", "Player5"))
        self.label_11.setText(_translate("MainWindow", "$0"))
        self.label_12.setText(_translate("MainWindow", "$0"))
        self.label_13.setText(_translate("MainWindow", "$0"))
        self.label_14.setText(_translate("MainWindow", "$0"))
        self.pushButton_7.setText(_translate("MainWindow", "$200"))
        self.pushButton_8.setText(_translate("MainWindow", "$200"))
        self.pushButton_9.setText(_translate("MainWindow", "$200"))
        self.pushButton_10.setText(_translate("MainWindow", "$200"))
        self.pushButton_11.setText(_translate("MainWindow", "$200"))
        self.pushButton_12.setText(_translate("MainWindow", "$400"))
        self.pushButton_13.setText(_translate("MainWindow", "$400"))
        self.pushButton_14.setText(_translate("MainWindow", "$600"))
        self.pushButton_15.setText(_translate("MainWindow", "$800"))
        self.pushButton_16.setText(_translate("MainWindow", "$1000"))
        self.pushButton_17.setText(_translate("MainWindow", "$400"))
        self.pushButton_18.setText(_translate("MainWindow", "$400"))
        self.pushButton_19.setText(_translate("MainWindow", "$400"))
        self.pushButton_20.setText(_translate("MainWindow", "$400"))
        self.pushButton_21.setText(_translate("MainWindow", "$600"))
        self.pushButton_22.setText(_translate("MainWindow", "$600"))
        self.pushButton_23.setText(_translate("MainWindow", "$600"))
        self.testbutton600.setText(_translate("MainWindow", "$1200"))
        self.pushButton_25.setText(_translate("MainWindow", "$600"))
        self.pushButton_26.setText(_translate("MainWindow", "$800"))
        self.pushButton_27.setText(_translate("MainWindow", "$800"))
        self.pushButton_28.setText(_translate("MainWindow", "$800"))
        self.pushButton_29.setText(_translate("MainWindow", "$800"))
        self.pushButton_30.setText(_translate("MainWindow", "$1600"))
        self.pushButton_31.setText(_translate("MainWindow", "$1000"))
        self.pushButton_32.setText(_translate("MainWindow", "$1000"))
        self.testbutton2000.setText(_translate("MainWindow", "$2000"))
        self.pushButton_34.setText(_translate("MainWindow", "$1000"))
        self.pushButton_35.setText(_translate("MainWindow", "$1000"))
        self.pushButton_2.setText(_translate("MainWindow", "Cat1"))
        self.pushButton_3.setText(_translate("MainWindow", "Cat1"))
        self.pushButton_4.setText(_translate("MainWindow", "Cat1"))
        self.pushButton_5.setText(_translate("MainWindow", "Cat1"))
        self.pushButton_6.setText(_translate("MainWindow", "Cat1"))
        self.pushButton_36.setText(_translate("MainWindow", "$800"))
        self.pushButton_24.setText(_translate("MainWindow", "X"))
        self.label_15.setText(_translate("MainWindow", "Player1"))
        self.label_18.setText(_translate("MainWindow", "Player1"))
        self.label_19.setText(_translate("MainWindow", "Player1"))
        self.label_20.setText(_translate("MainWindow", "Player1"))
        self.label_21.setText(_translate("MainWindow", "Player1"))
        self.label_22.setText(_translate("MainWindow", "$0"))
        self.label_23.setText(_translate("MainWindow", "$0"))
        self.label_24.setText(_translate("MainWindow", "$0"))
        self.label_25.setText(_translate("MainWindow", "$0"))
        self.label_26.setText(_translate("MainWindow", "$0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
