from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from screens.home_screen import HomeScreen
from screens.question_screen import QuestionScreen
from screens.answer_screen import AnswerScreen

class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeopardy Game")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home_screen = HomeScreen(self)
        self.question_screen = QuestionScreen(self)
        self.answer_screen = AnswerScreen(self)

        self.stacked_widget.addWidget(self.home_screen)
        self.stacked_widget.addWidget(self.question_screen)
        self.stacked_widget.addWidget(self.answer_screen)

    def show_home_screen(self):
        self.stacked_widget.setCurrentWidget(self.home_screen)

    def show_question_screen(self):
        self.stacked_widget.setCurrentWidget(self.question_screen)

    def show_answer_screen(self):
        self.stacked_widget.setCurrentWidget(self.answer_screen)
