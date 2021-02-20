import random
import sys
from PyQt5 import QtCore, QtWidgets, QtGui

from welcome.welcome import Welcome
from welcome.info import Info
from Category.category import Category
from Game.game_UI import Game

def summa(): pass

def welcome_screen():
    welcome_scr = Welcome()
    widget.addWidget(welcome_scr)
    widget.setCurrentWidget(welcome_scr)

    welcome_scr.StartGame.setShortcut('Return')
    welcome_scr.Info.setShortcut('F1')
    welcome_scr.StartGame.clicked.connect(lambda:category_screen())
    welcome_scr.Info.clicked.connect(lambda:info_screen())
    
    welcome_scr.esc = QtWidgets.QShortcut('Esc', welcome_scr)
    welcome_scr.esc.activated.connect(summa)
    
def info_screen():
    info_scr = Info()
    
    this = widget.currentWidget()
    
    widget.addWidget(info_scr.Dialog)
    widget.setCurrentWidget(info_scr.Dialog)
    widget.removeWidget(this)
    
    info_scr.buttonBox.accepted.connect(welcome_screen)
    info_scr.buttonBox.rejected.connect(welcome_screen)    
    QtCore.QMetaObject.connectSlotsByName(info_scr.Dialog)
    
    info_scr.esc = QtWidgets.QShortcut('Esc', info_scr.Dialog)
    info_scr.esc.activated.connect(welcome_screen)
    
    
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
        
        if move is True: game_screen(word, hint,key)
    
    category_scr = Category()
    
    this = widget.currentWidget()
    
    widget.addWidget(category_scr)
    widget.setCurrentWidget(category_scr)
    widget.removeWidget(this)
    
    category_scr.StartButton.clicked.connect(click)
    
    category_scr.esc = QtWidgets.QShortcut('Esc', category_scr)
    category_scr.esc.activated.connect(welcome_screen)
    
    
def game_screen(word,hint,topic):
    print(word,hint)
    game_scr = Game(word,hint,topic)
    this = widget.currentWidget()
    
    widget.addWidget(game_scr.Dialog)
    widget.setCurrentWidget(game_scr.Dialog)
    widget.removeWidget(this)
    
    game_scr.esc = QtWidgets.QShortcut('Esc', game_scr.Dialog)
    game_scr.esc.activated.connect(category_screen)

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