import sys
from PyQt5.QtWidgets import QApplication
from controller import Controller

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()  # Ensure the controller is shown
    controller.show_home_screen()  # Show the initial home screen
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
