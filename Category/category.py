from os import set_blocking
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
import sys, json

class Category(QtWidgets.QDialog):

    def __init__(self):
        super(QtWidgets.QDialog, self).__init__()
        loadUi('Tests/Category/category.ui', self)

        with open('wordlist.json') as f:
            self.data = json.load(f)
            self.keys = [i for i in self.data.keys()]
            self.all  = [j for i in self.keys for j in self.data[i]]
        # print(self.keys, type(self.keys))
        # self.StartButton.clicked.connect(lambda:print('start clicked'))
        self.list()


    def list(self):
                
        for i in range(len(self.keys)):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setPointSize(20)
            item.setFont(font)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(self.keys[i])
            self.listWidget.addItem(item)
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Category())
    widget.show()
    sys.exit(app.exec_())