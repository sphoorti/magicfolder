# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adddialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ConfigParser
import sys

class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(500, 500)
        self.extLabel = QtWidgets.QLabel(AddDialog)
        self.extLabel.setGeometry(QtCore.QRect(30, 40, 81, 21))
        self.extLabel.setObjectName("extLabel")
        self.targetLabel = QtWidgets.QLabel(AddDialog)
        self.targetLabel.setGeometry(QtCore.QRect(30, 90, 101, 21))
        self.targetLabel.setObjectName("targetLabel")
        self.buttonBox = QtWidgets.QDialogButtonBox(AddDialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 160, 176, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(AddDialog.accept)
        self.buttonBox.rejected.connect(AddDialog.reject)
        self.extLineEdit = QtWidgets.QLineEdit(AddDialog)
        self.extLineEdit.setGeometry(QtCore.QRect(140, 40, 113, 33))
        self.extLineEdit.setObjectName("extLineEdit")
        self.targetLineEdit = QtWidgets.QLineEdit(AddDialog)
        self.targetLineEdit.setGeometry(QtCore.QRect(140, 90, 113, 33))
        self.targetLineEdit.setObjectName("targetLineEdit")

        self.retranslateUi(AddDialog)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDialog.setWindowTitle(_translate("AddDialog", "AddDialog"))
        self.extLabel.setText(_translate("AddDialog", "Extensions :"))
        self.targetLabel.setText(_translate("AddDialog", "<html><head/><body><p>Target folder :</p></body></html>"))
