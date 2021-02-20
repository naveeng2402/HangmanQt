from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random, string

class Game():
    
    '''
    # Widgets to be changed:\n
        \t self.hintLabel.setToolTip()\n
        \t self.topicNameLabel.setText()\n
        \t self.dispLabel.setText('Game Text')\n
        \t self.dispList\n

    '''
    
    def __init__(self, word:str, hint:str, topic:str):
        
        self.word = word.upper()
        self.topic = topic.capitalize()
        self.hint = hint.title()
        self.options = [self.word[i]+str(i) for i in range(len(self.word))]
        if len(self.options)<10: self.options.extend(random.choices(string.ascii_uppercase,k=10-len(self.options)))
        random.shuffle(self.options)
        self.dispLst = ['_' for i in range(len(self.word))]
        self.Dialog = QtWidgets.QDialog()
        self.setup()
        
    def setup(self):
        self.Dialog.setObjectName('Dialog')
        self.Dialog.resize(600,400)
        self.gridlayout = QtWidgets.QGridLayout(self.Dialog)
        self.gridlayout.setObjectName('gridlayout')
        
        self.rootFrame = QtWidgets.QFrame(self.Dialog)
        self.rootFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rootFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rootFrame.setObjectName("rootFrame")
        self.gridlayout.addWidget(self.rootFrame)
        
        self.rootLayout = QtWidgets.QGridLayout(self.rootFrame)
        self.rootLayout.setObjectName('rootLayout')
        
        self.titleFrame = QtWidgets.QFrame(self.rootFrame)
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.titleFrame.setObjectName("titleFrame")
        self.rootLayout.addWidget(self.titleFrame,0,0,1,5)
        
        self.titleLayout = QtWidgets.QHBoxLayout(self.titleFrame)
        self.titleLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLayout.setSpacing(0)
        self.titleLayout.setObjectName("titleLayout")
        
        self.titleFont = QtGui.QFont('Ubuntu', 30)
        
        self.titleText = QtWidgets.QLabel(self.titleFrame)
        titleFont = QtGui.QFont()
        titleFont.setPointSize(20)
        self.titleText.setFont(titleFont)
        self.titleText.setAlignment(QtCore.Qt.AlignCenter)
        self.titleText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.titleText.setText('HANGMAN')
        self.titleText.setFont(self.titleFont)
        self.titleText.setObjectName("titleText")   
        self.titleLayout.addWidget(self.titleText)    
        
        self.imageFrame = QtWidgets.QFrame(self.rootFrame) 
        self.imageFrame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.imageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imageFrame.setObjectName("imageFrame")
        self.rootLayout.addWidget(self.imageFrame,1,0,1,2)
        
        self.imageLayout = QtWidgets.QGridLayout(self.imageFrame)
        self.imageLayout.setContentsMargins(0, 0, 0, 0)
        self.imageLayout.setSpacing(0)
        self.imageLayout.setObjectName("imageLayout")
        
        self.image = QtWidgets.QLabel(self.imageFrame)
        self.image.setStyleSheet('''
                                 border-image: url(Images/Five/Hangman5.svg)
                                 ''')
        self.imageLayout.addWidget(self.image)
        
        self.gameFrame = QtWidgets.QFrame(self.rootFrame)
        self.gameFrame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.gameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameFrame.setObjectName('gameFrame')
        self.rootLayout.addWidget(self.gameFrame,1,2,1,3)
        
        self.gameLayout = QtWidgets.QVBoxLayout(self.gameFrame)
        self.gameLayout.setObjectName('gameLayout')
        
        self.hintFrame = QtWidgets.QFrame(self.gameFrame)
        self.hintFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hintFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hintFrame.setObjectName('hintFrame')
        self.gameLayout.addWidget(self.hintFrame)
        
        self.hintLayout = QtWidgets.QHBoxLayout(self.hintFrame)
        self.hintLayout.setObjectName('hintLayout')
        
        self.hintSpace  = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hintLayout.addItem(self.hintSpace)
        
        self.hintLabel = QtWidgets.QLabel(self.hintFrame)
        self.hintLabel.setText('''<p><span style="text-decoration: underline; font-size: 20px;"><strong>HINT</strong></span></p>
        <p><span style="text-decoration: underline; font-size: 10px; color: #ff0000;">(hover here)</span></p>''')
        self.hintLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hintLabel.setToolTip(self.hint)
        self.hintLabel.setObjectName('hintLabel')
        self.hintLayout.addWidget(self.hintLabel)
        
        self.topicFrame = QtWidgets.QFrame(self.gameFrame)
        self.topicFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topicFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topicFrame.setObjectName('topicFrame')
        self.gameLayout.addWidget(self.topicFrame)      
        
        self.topicLayout = QtWidgets.QHBoxLayout(self.topicFrame)
        self.topicLayout.setObjectName('topicLayout')
        
        self.topicFont = QtGui.QFont('Ubuntu', 20)
        
        self.topicLabel = QtWidgets.QLabel(self.topicFrame)
        self.topicLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topicLabel.setText('Topic : ')
        self.topicLabel.setFont(self.topicFont)
        self.topicLabel.setObjectName('topicLabel')
        self.topicLayout.addWidget(self.topicLabel)
            
        self.topicNameLabel = QtWidgets.QLabel(self.topicFrame)
        self.topicNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topicNameLabel.setText(self.topic)
        self.topicNameLabel.setFont(self.topicFont)        
        self.topicNameLabel.setObjectName('topicNameLabel')
        self.topicLayout.addWidget(self.topicNameLabel) 
        
        self.dispFont = QtGui.QFont('Ubuntu',50)
        
        self.dispLabel = QtWidgets.QLabel(self.gameFrame)
        self.dispLabel.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.dispLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dispLabel.setText(' '.join(self.dispLst))
        self.dispLabel.setFont(self.dispFont)
        self.dispLabel.setObjectName('dispLabel')
        self.gameLayout.addWidget(self.dispLabel)
        
        self.buttonFrame = QtWidgets.QFrame(self.gameFrame)
        self.buttonFrame.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.buttonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttonFrame.setObjectName('buttonFrame')
        self.gameLayout.addWidget(self.buttonFrame)
        
        self.buttonLayout = QtWidgets.QGridLayout(self.buttonFrame)
        self.buttonLayout.setObjectName('buttonLayout')
        
        self.buttonFont = QtGui.QFont('Ubuntu',20)
        
        self.button_gen()
        
    def button_gen(self):  
        
        row = -1
        
        for i in range(len(self.options)):
            if i%5 == 0: row +=1
            exec(f'''self.{'B_'+self.options[i]} = QtWidgets.QPushButton(self.buttonFrame)''')
            eval(f'''self.{'B_'+self.options[i]}.setMinimumSize(50,50)''')
            eval(f'''self.{'B_'+self.options[i]}.setFont(self.buttonFont)''')
            eval(f'''self.ss(self.{'B_'+self.options[i]})''')
            eval(f'''self.{'B_'+self.options[i]}.setText('{self.options[i][0]}')''')
            eval(f'''self.{'B_'+self.options[i]}.setObjectName("{'B_'+self.options[i]}")''')
            eval(f'''self.buttonLayout.addWidget(self.{'B_'+self.options[i]},{row},{i%5})''')
        
    def ss(self,btn:QtWidgets.QPushButton, color:str = 'white'):
        buttonSS = f'''QPushButton::!hover
                                {{
                                    border-radius: 25px;
                                    border: 3px solid black;
                                    background-color: {color};
                                    color:black;
                                }}

                            QPushButton::hover
                                {{
                                    border-radius: 25px;
                                    border: 3px solid black;
                                    background-color: lightblue;
                                }}

                            QPushButton::pressed
                                {{
                                    border-radius: 25px;
                                    border: 3px solid black;
                                    background-color: hsv(60,50%,100%);
                                }}'''
        btn.setStyleSheet(buttonSS)
        
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen = Game('naveen')
    # screen.Dialog.show()
    screen.Dialog.showMaximized()
    sys.exit(app.exec_())