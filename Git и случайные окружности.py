from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
import random
from AppInterface import Ui_MainWindow


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paint = False
        self.but.clicked.connect(self.paint_start)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_smile(qp)
            qp.end()

    def paint_start(self):
        self.paint = True

    def draw_smile(self, qp):
        x = random.randrange(10, 300)
        y = random.randrange(10, 300)
        r = random.randrange(1, 255)
        g = random.randrange(1, 255)
        b = random.randrange(1, 255)
        qp.setPen(QColor(r, g, b))
        qp.drawEllipse(x, y, x, y)

        x = random.randrange(10, 300)
        y = random.randrange(10, 300)
        r = random.randrange(1, 255)
        g = random.randrange(1, 255)
        b = random.randrange(1, 255)
        qp.setPen(QColor(r, g, b))
        qp.drawEllipse(x, y, x, y)
        self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
