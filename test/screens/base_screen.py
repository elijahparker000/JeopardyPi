from PyQt5.QtWidgets import QWidget

class BaseScreen(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        pass
