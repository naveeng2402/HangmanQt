from PyQt5 import QtWidgets, QtCore

class Info():
    
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        
        self.setup()
        self.Dialog.show()
        
    def setup(self):
        
        self.Dialog.setObjectName("Dialog")
        
        self.layout = QtWidgets.QVBoxLayout(self.Dialog)
        self.layout.setObjectName('Layout')
        
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.layout.addWidget(self.textBrowser)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.layout.addWidget(self.buttonBox)
        
