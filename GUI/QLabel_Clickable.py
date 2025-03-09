import random
from PySide6.QtCore import Signal  # , QObject,
from PySide6.QtWidgets import QLabel
# from PySide6.QtGui import *


class QLabel_Clickable(QLabel):
    clicked = Signal()
    life_status = 0
    myname = ""

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()

    def change_status(self, status):
        self.life_status = status

    def change_status_random(self):
        self.life_status = random.randint(0, 1)

    def tell_status(self):
        return self.life_status

    def give_myname(self, name):
        self.myname = name

    def tell_myname(self):
        return self.myname
