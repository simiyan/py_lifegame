import random
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import *

class QLabel_Clickable(QLabel):
    clicked=pyqtSignal()
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
    