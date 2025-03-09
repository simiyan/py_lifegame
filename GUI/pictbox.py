# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pictbox.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDialog, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(450, 309)
        self.btnWorldTick = QPushButton(Dialog)
        self.btnWorldTick.setObjectName(u"btnWorldTick")
        self.btnWorldTick.setGeometry(QRect(10, 30, 100, 30))
        self.btnRandomSet = QPushButton(Dialog)
        self.btnRandomSet.setObjectName(u"btnRandomSet")
        self.btnRandomSet.setGeometry(QRect(120, 30, 100, 30))
        self.cmbInitialData = QComboBox(Dialog)
        self.cmbInitialData.setObjectName(u"cmbInitialData")
        self.cmbInitialData.setGeometry(QRect(340, 30, 80, 30))
        self.btnStopPause = QPushButton(Dialog)
        self.btnStopPause.setObjectName(u"btnStopPause")
        self.btnStopPause.setGeometry(QRect(230, 0, 100, 30))
        self.lblGeneration = QLabel(Dialog)
        self.lblGeneration.setObjectName(u"lblGeneration")
        self.lblGeneration.setGeometry(QRect(10, 10, 50, 12))
        self.lblGeneration.setLayoutDirection(Qt.LeftToRight)
        self.lblGeneration.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txtLifeStatus = QTextEdit(Dialog)
        self.txtLifeStatus.setObjectName(u"txtLifeStatus")
        self.txtLifeStatus.setGeometry(QRect(10, 70, 411, 70))
        self.txtLifeStatus.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.txtLifeStatus.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.txtLifeStatus.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.txtLifeStatus.setReadOnly(True)
        self.btnReset = QPushButton(Dialog)
        self.btnReset.setObjectName(u"btnReset")
        self.btnReset.setGeometry(QRect(230, 30, 100, 30))
        self.chkRemovePict = QCheckBox(Dialog)
        self.chkRemovePict.setObjectName(u"chkRemovePict")
        self.chkRemovePict.setGeometry(QRect(340, 10, 81, 16))
        self.chkRemovePict.setChecked(True)
        self.lblWorldNoText = QLabel(Dialog)
        self.lblWorldNoText.setObjectName(u"lblWorldNoText")
        self.lblWorldNoText.setGeometry(QRect(70, 10, 50, 12))
        self.lblWorldNoText.setLayoutDirection(Qt.LeftToRight)
        self.lblWorldNoText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblWorldNo = QLabel(Dialog)
        self.lblWorldNo.setObjectName(u"lblWorldNo")
        self.lblWorldNo.setGeometry(QRect(120, 10, 50, 12))
        self.lblWorldNo.setLayoutDirection(Qt.LeftToRight)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btnWorldTick.setText(QCoreApplication.translate("Dialog", u"WorldStart", None))
        self.btnRandomSet.setText(QCoreApplication.translate("Dialog", u"Random", None))
        self.btnStopPause.setText(QCoreApplication.translate("Dialog", u"StopPause", None))
        self.lblGeneration.setText(QCoreApplication.translate("Dialog", u"\u4e16\u4ee3", None))
        self.btnReset.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.chkRemovePict.setText(QCoreApplication.translate("Dialog", u"RemovePict", None))
        self.lblWorldNoText.setText(QCoreApplication.translate("Dialog", u"world_no\uff1a", None))
        self.lblWorldNo.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

