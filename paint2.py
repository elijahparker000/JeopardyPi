# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import ImageQt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QLabel):
  def __init__(self):
    super().__init__()

    #self.label = QtWidgets.QLabel()
    #canvas = QtGui.QPixmap(300, 50)
    #canvas.fill(Qt.blue)
    #self.label.setPixmap(canvas)
    #self.setCentralWidget(self.label)

    pixmap = QtGui.QPixmap(900, 150)
    pixmap.fill(Qt.white)
    self.setPixmap(pixmap)

    self.last_x, self.last_y = None, None

    self.add = QShortcut(QKeySequence("Ctrl+S"), self)
    self.add.activated.connect(self.compositeEvent)

  def mouseMoveEvent(self, e):
    if self.last_x is None: # First event.
      self.last_x = e.x()
      self.last_y = e.y()
      return # Ignore the first time.

    #painter = QtGui.QPainter(self.label.pixmap())
    #painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
    #painter.end()
    #self.update()

    painter = QtGui.QPainter(self.pixmap())
    p = painter.pen()
    p.setWidth(4)
    p.setColor(QtGui.QColor('blue'))
    painter.setPen(p)
    painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
    painter.end()
    self.update()

    # Update the origin for next time.
    self.last_x = e.x()
    self.last_y = e.y()

  def mouseReleaseEvent(self, e):
    self.last_x = None
    self.last_y = None
    self.compositeEvent()
      
  def compositeEvent(self):
    image = ImageQt.fromqpixmap(self.pixmap())
    image.save('test.png')


if __name__ == '__main__':
  app = QApplication([])
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())