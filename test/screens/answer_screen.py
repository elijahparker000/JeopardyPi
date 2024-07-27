from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from .base_screen import BaseScreen

class AnswerScreen(BaseScreen):
    def __init__(self, controller):
        super().__init__(controller)

    def init_ui(self):
        layout = QVBoxLayout()

        answer_label = QLabel("This is the answer.")
        layout.addWidget(answer_label)

        home_button = QPushButton("Back to Home")
        home_button.clicked.connect(self.controller.show_home_screen)
        layout.addWidget(home_button)

        self.setLayout(layout)
        print("Answer screen initialized")
