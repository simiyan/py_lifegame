# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pictbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 296)
        self.btnWorldTick = QtWidgets.QPushButton(Dialog)
        self.btnWorldTick.setGeometry(QtCore.QRect(10, 30, 100, 30))
        self.btnWorldTick.setObjectName("btnWorldTick")
        self.btnRandomSet = QtWidgets.QPushButton(Dialog)
        self.btnRandomSet.setGeometry(QtCore.QRect(120, 30, 100, 30))
        self.btnRandomSet.setObjectName("btnRandomSet")
        self.cmbInitialData = QtWidgets.QComboBox(Dialog)
        self.cmbInitialData.setGeometry(QtCore.QRect(340, 30, 80, 30))
        self.cmbInitialData.setObjectName("cmbInitialData")
        self.btnStopPause = QtWidgets.QPushButton(Dialog)
        self.btnStopPause.setGeometry(QtCore.QRect(230, 0, 100, 30))
        self.btnStopPause.setObjectName("btnStopPause")
        self.lblGeneration = QtWidgets.QLabel(Dialog)
        self.lblGeneration.setGeometry(QtCore.QRect(10, 10, 50, 12))
        self.lblGeneration.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblGeneration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblGeneration.setObjectName("lblGeneration")
        self.txtLifeStatus = QtWidgets.QTextEdit(Dialog)
        self.txtLifeStatus.setGeometry(QtCore.QRect(10, 70, 411, 70))
        self.txtLifeStatus.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtLifeStatus.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtLifeStatus.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.txtLifeStatus.setReadOnly(True)
        self.txtLifeStatus.setObjectName("txtLifeStatus")
        self.btnReset = QtWidgets.QPushButton(Dialog)
        self.btnReset.setGeometry(QtCore.QRect(230, 30, 100, 30))
        self.btnReset.setObjectName("btnReset")
        self.chkRemovePict = QtWidgets.QCheckBox(Dialog)
        self.chkRemovePict.setGeometry(QtCore.QRect(340, 10, 81, 16))
        self.chkRemovePict.setChecked(True)
        self.chkRemovePict.setObjectName("chkRemovePict")
        self.lblWorldNoText = QtWidgets.QLabel(Dialog)
        self.lblWorldNoText.setGeometry(QtCore.QRect(70, 10, 50, 12))
        self.lblWorldNoText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblWorldNoText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWorldNoText.setObjectName("lblWorldNoText")
        self.lblWorldNo = QtWidgets.QLabel(Dialog)
        self.lblWorldNo.setGeometry(QtCore.QRect(120, 10, 50, 12))
        self.lblWorldNo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblWorldNo.setObjectName("lblWorldNo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnWorldTick.setText(_translate("Dialog", "WorldStart"))
        self.btnRandomSet.setText(_translate("Dialog", "Random"))
        self.btnStopPause.setText(_translate("Dialog", "StopPause"))
        self.lblGeneration.setText(_translate("Dialog", "世代"))
        self.btnReset.setText(_translate("Dialog", "Reset"))
        self.chkRemovePict.setText(_translate("Dialog", "RemovePict"))
        self.lblWorldNoText.setText(_translate("Dialog", "world_no："))
        self.lblWorldNo.setText(_translate("Dialog", "0"))
