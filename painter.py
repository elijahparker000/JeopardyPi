import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen

image_path = "C:/Users/elija/OneDrive/Pictures/dogoo.jpg"



class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap(image_path)
    
    def paintEvent(self, event):
        
        #draw on image
        pen = QPen()
        pen.setWidth(5)

        #upload Image
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.setPen(pen)
        painter.drawEllipse(150, 150, 150, 150)

         


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

    sys.exit(app.exec())

main()
