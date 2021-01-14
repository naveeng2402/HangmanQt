import json
import sys
from PyQt5 import QtCore, QtWidgets, QtGui

from welcome.welcome import Welcome
from welcome.info import Info


def welcome_screen():
    welcome_scr = Welcome()
    widget.addWidget(welcome_scr)
    widget.setCurrentWidget(welcome_scr)
    
    welcome_scr.StartGame.clicked.connect(lambda:print("StartGame clicked"))
    welcome_scr.Info.clicked.connect(info_screen)
    
def info_screen():
    info_scr = Info()
    
    this = widget.currentWidget()
    
    widget.addWidget(info_scr.Dialog)
    widget.setCurrentWidget(info_scr.Dialog)
    widget.removeWidget(this)
    
    info_scr.buttonBox.accepted.connect(welcome_screen)
    info_scr.buttonBox.rejected.connect(welcome_screen)    
    QtCore.QMetaObject.connectSlotsByName(info_scr.Dialog)
    
    


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle('Hangman')
    widget.resize(400, 300)
    # widget.setWindowIcon(QtGui.QIcon('Others/icon.svg'))
    
    welcome_screen()
    
    widget.show()
    sys.exit(app.exec_())