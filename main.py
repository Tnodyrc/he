import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class What(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False


    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(10, 100)
        qp.drawEllipse(randint(75, 400), randint(25, 300), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = What()
    ex.show()
    sys.exit(app.exec())