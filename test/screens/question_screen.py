from PyQt5.QtWidgets import QVBoxLayout, QPushButton
from .base_screen import BaseScreen

class QuestionScreen(BaseScreen):
    def __init__(self, controller):
        super().__init__(controller)

    def init_ui(self):
        layout = QVBoxLayout()

        question_button = QPushButton("Show Answer")
        question_button.clicked.connect(self.controller.show_answer_screen)
        layout.addWidget(question_button)

        self.setLayout(layout)
        print("Question screen initialized")
