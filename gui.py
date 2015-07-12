import sys
import ConfigParser
from PyQt5.QtWidgets import (QDialog, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QComboBox)
from PyQt5.QtCore import Qt
from adddialog import Ui_AddDialog

class AddRuleWindow(QDialog, Ui_AddDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)

class Main_Gui(QWidget):
    def __init__(self):
	super(Main_Gui, self).__init__()
        self.fileType = 'Text'
	self.initUI()

    def initUI(self):
        combo = QComboBox(self)
        combo.addItem("Text")
        combo.addItem("Video")
        combo.addItem("Image")
        combo.move(20, 20)
        combo.activated[str].connect(self.onActivated)
        self.addbtn = QPushButton('Add Rule', self)
        self.addbtn.move(100, 20)
        self.addbtn.clicked.connect(self.addRuleDialog)
        self.delbtn = QPushButton('Delete Rule', self)
        self.delbtn.move(200, 20)
        self.delbtn.clicked.connect(self.delRuleDialog)
        self.modbtn = QPushButton('Modify Rule', self)
        self.modbtn.move(310, 20)
        self.modbtn.clicked.connect(self.modRuleDialog)
        self.resize(500, 500)
        self.setWindowTitle('Magic Folder')

    def onActivated(self, text):
        self.fileType = text

    def addRuleDialog(self):
        extStr = ''
        config = ConfigParser.RawConfigParser()
        config.readfp(open('rules.ini'))
        extList = config.get(self.fileType, 'extensions')
        for item in extList:
            extStr += item
        print extStr
        addwid = AddRuleWindow(self)
        result = addwid.exec_()
        addwid.extLineEdit.setText(extStr)
        if result == QDialog.Accepted:
            #write to rules.ini
            #provide tooltip to add comma between 2 ext or write logic to split otherwise
            config.set(self.fileType, 'extensions', addwid.extLineEdit.text())
            with open('rules.ini', 'wb') as configfile:
                config.write(configfile)

    def delRuleDialog(self):
        print 'Delete Rule'

    def modRuleDialog(self):
        print 'Modify Rule'

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = Main_Gui()
    ui.show()
    sys.exit(app.exec_())
