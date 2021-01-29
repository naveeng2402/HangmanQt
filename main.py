import random
import sys
from PyQt5 import QtCore, QtWidgets, QtGui

from welcome.welcome import Welcome
from welcome.info import Info
from Category.category import Category


def welcome_screen():
    welcome_scr = Welcome()
    widget.addWidget(welcome_scr)
    widget.setCurrentWidget(welcome_scr)
    
    welcome_scr.StartGame.clicked.connect(category_screen)
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
    
    
def category_screen():
    
    def click():
        select = category_scr.listWidget.selectedItems()
        move = False
        
        if len(select) > 0:
            key = select[0].text()
            data = ''
            word = ''
            hint = ''
            if key == 'ALL':
                data = category_scr.all
            else:
                data = category_scr.data[key]
            
            word = random.choice(data)
            
            if type(word) == list:
                word, hint = word[0], word[1]
            else:
                hint = "Hint Not Available"
                        
            move = True
            # print(key)
            # print(data)
            # print(word)
            # print(hint)
        
        if move is True: game_screen(word, hint)
    
    category_scr = Category()
    
    this = widget.currentWidget()
    
    widget.addWidget(category_scr)
    widget.setCurrentWidget(category_scr)
    widget.removeWidget(this)
    
    category_scr.StartButton.clicked.connect(click)
    
    
def game_screen(word,hint):
    print(word,hint)


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