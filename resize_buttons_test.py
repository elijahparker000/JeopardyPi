import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtCore import QSize
import resources_rc

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()

        values = ['1', '2', '3', 
                  '4', '5', '6', 
                  '7', '8', '9']
        positions = [(r, c) for r in range(3) for c in range(3)]

        self.layoutGrid = QGridLayout()
        self.setLayout(self.layoutGrid)

        self.buttons = []
        for position, value in zip(positions, values):
            print('Coordinate: ' + str(position) + ' with value of ' + str(value))
            button = QPushButton()
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            icon = QIcon(":/images/png/dollar_200.png")
            button.setIcon(icon)
            button.setIconSize(button.size())
            self.layoutGrid.addWidget(button, *position)
            self.buttons.append(button)

        self.resize_to_screen()

    def resize_to_screen(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.setGeometry(screen_geometry)
        self.resizeIcons()

    def resizeIcons(self):
        for button in self.buttons:
            button.setIconSize(button.size())


def main():
    app = QApplication(sys.argv)
    demo = GridDemo()
    #demo.showMaximized()  # Show the window maximized
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
