import sys
from PyQt5.QtWidgets import QApplication, QGroupBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QScreen
from test import Ui_GroupBox  # Import the generated UI file

class MyApp(QGroupBox):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.button_clicked)  # Connect the signal here

        self.init_ui()

    def init_ui(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.setGeometry(screen_geometry)
        self.showMaximized()

    def resizeEvent(self, event):
        # Handle resizing here if needed, layouts should automatically handle resizing
        super().resizeEvent(event)

    def button_clicked(self):
        print("BUTTON PRESSED")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
