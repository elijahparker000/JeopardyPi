from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from .base_screen import BaseScreen

class HomeScreen(BaseScreen):
    def __init__(self, controller):
        super().__init__(controller)

    def init_ui(self):
        layout = QVBoxLayout()

        start_button = QPushButton("Start Game")
        start_button.clicked.connect(self.controller.show_question_screen)
        layout.addWidget(start_button)

        self.setLayout(layout)
        print("Home screen initialized")
