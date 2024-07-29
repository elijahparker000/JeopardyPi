import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import Qt, QRect

class AspectRatioWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.aspect_ratio = 16 / 9  # Aspect ratio (e.g., 16:9)

        # Layout and button setup
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.fit_button = QPushButton("Fit to Screen", self)
        self.fit_button.clicked.connect(self.fit_to_screen)
        layout.addWidget(self.fit_button)

        self.setWindowTitle("Aspect Ratio Demo")

    def fit_to_screen(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        
        # Get screen dimensions
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        
        # Calculate new dimensions while maintaining the aspect ratio
        new_width = screen_width
        new_height = int(new_width / self.aspect_ratio)
        
        if new_height > screen_height:
            new_height = screen_height
            new_width = int(new_height * self.aspect_ratio)
        
        # Resize and center the window
        self.setGeometry(
            QRect(
                (screen_width - new_width) // 2,
                (screen_height - new_height) // 2,
                new_width,
                new_height,
            )
        )

def main():
    app = QApplication(sys.argv)
    demo = AspectRatioWidget()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
