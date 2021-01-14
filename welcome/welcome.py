from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi
import sys

class Welcome(QtWidgets.QDialog):
    
    def __init__(self):
        super(QtWidgets.QDialog, self).__init__()
        loadUi("Tests/Welcome/welcome.ui", self)
        self.Image.setStyleSheet("""
                                   border-image: url(Images/Ten/Hangman10.svg);
                                """)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Welcome())
    widget.show()
    sys.exit(app.exec_())