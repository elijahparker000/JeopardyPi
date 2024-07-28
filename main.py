import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from jeopardy_board import Ui_JeopardyBoard  # Import the generated UI file
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Add the project root to the Python path
project_root = os.getenv('PROJ_PATH')
if project_root not in sys.path:
    sys.path.append(project_root)

import resources_rc  # Import the generated resource file

class JeopardyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JeopardyBoard()
        self.ui.setupUi(self)
        self.ui.buttonClicked.connect(self.print_button_name)  # Connect the custom signal

    def print_button_name(self, button_name):
        print(f"Button pressed: {button_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        window = JeopardyApp()
        window.showMaximized()  # To start the window maximized
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")
