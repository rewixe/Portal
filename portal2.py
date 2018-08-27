from PyQt4.QtCore import *
from PyQt4.QtGui import *
from functools import partial
import locale
import time
import sys

class portal(QWidget):

    def __init__(self):
        super(portal, self).__init__()
        self.langchoice=""
        self.initUI()
        self.loadlocales()

    ##Initalises user interface
    def initUI(self):
        self.w = QWidget()
        self.w.resize(800, 700)
        self.w.move(500, 100) 
        self.w.setWindowTitle('Software for the Global Market II - Lab 1')
        self.w.setWindowIcon(QIcon('Logo.png'))

        ##functions
        self.css()
        self.createButtons()
        self.createEntry()
        self.w.show()

    ##functions which opens .css file, sets style of the windows
    def css(self):
        self.styledata=' '
        file=open('portal.css','r')
        self.styledata=file.read()
        file.close()
        self.w.setStyleSheet(self.styledata)

    ##Function to create the first window the user sees, the 'entry' window 
    def createEntry(self):
        self.nameLabel = QLabel(self.w)  ##Shows portal name
        self.nameLabel.setGeometry(QRect(240, 30, 550, 80))
        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(55)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setText("Overseas Study Portal")
        
        self.entryLabel = QLabel(self.w)  ##Welcomes user to the interface
        self.entryLabel.setGeometry(QRect(280, 150, 550, 40))
        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(55)
        self.entryLabel.setFont(font)
        self.entryLabel.setObjectName("entryLabel")
        self.entryLabel.setText("Welcome to the Student Portal!")

        ##User is asked to select language in multiple languages, to ensure the user understands
        self.introLabel = QLabel(self.w) ##Asks the user to select a language in English
        self.introLabel.setGeometry(QRect(300, 180, 550, 50))
        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(55)
        self.introLabel.setFont(font)
        self.introLabel.setObjectName("introLabel")
        self.introLabel.setText("Please select a language")

        self.introLabelp = QLabel(self.w)  ##Asks the user to select a language in Polish
        self.introLabelp.setGeometry(QRect(420, 220, 550, 50))
        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(55)
        self.introLabelp.setFont(font)
        self.introLabelp.setObjectName("introLabel")
        self.introLabelp.setText("Proszę wybrać język")

        self.introLabelf = QLabel(self.w)  ##Asks the user to select a language in Filipino
        self.introLabelf.setGeometry(QRect(290, 260, 550, 50))
        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(55)
        self.introLabelf.setFont(font)
        self.introLabelf.setObjectName("introLabel")
        self.introLabelf.setText("Mangyaring pumili ng wika")

    ##Function to create buttons on entry window 
    def createButtons(self):
        
        with open('tracker.txt', 'r') as myfile:
            data=myfile.read().replace('\n', '')
        
        self.conBtn = QPushButton('Continue', self.w)  ##Continue buttons, moves user to the next screen
        self.conBtn.setGeometry(400, 600, 100, 50)
        self.conBtn.setToolTip('This is will take you to the home page')
        self.conBtn.move(400, 600)
        self.conBtn.clicked.connect(self.mainScreen)

        self.exBtn = QPushButton('Exit', self.w)  ##Buttons to exit the interface
        self.exBtn.setGeometry(250, 600, 100, 50)
        self.exBtn.setToolTip('Exit menu')
        self.exBtn.move(250, 600)
        self.exBtn.clicked.connect(self.exitBtn)

        self.enbtn = QRadioButton("English", self.w)  ##Radio button to allow user to select language
        self.enbtn.setGeometry(250, 200, 100, 80)
        self.enbtn.setToolTip('Set to English')
        self.enbtn.move(250, 350)
        self.enbtn.toggled.connect(partial(self.langButtonCheck,self.enbtn))
        if data == 'English':
             self.enbtn.setChecked(True)

        self.plbtn = QRadioButton("Polska", self.w)  ##Radio button to allow user to select language
        self.plbtn.setGeometry(450, 200, 150, 80)
        self.plbtn.setToolTip('Set to Polish')
        self.plbtn.move(400, 350)
        self.plbtn.toggled.connect(partial(self.langButtonCheck,self.plbtn))
        if data == 'Polska':
             self.plbtn.setChecked(True)

        self.phbtn = QRadioButton("Filipino", self.w)  ##Radio button to allow user to select language
        #self.phbtn.setChecked(True)
        self.phbtn.setGeometry(200, 300, 150, 80)
        self.phbtn.setToolTip('Set to Filipino')
        self.phbtn.move(350, 400)
        self.phbtn.toggled.connect(partial(self.langButtonCheck,self.phbtn))
        if data == 'Filipino':
             self.phbtn.setChecked(True)

    ##Locales
    def loadlocales(self):
        self.langs=['English', 'Polska', 'Filipino']
        self.rfolders=['en_IE', 'pl_PL', 'ph_PH']
        self.locales=['English_Ireland.1252', 'French_Canada.1252', 'Filipino_Philippines.1252']

    ##Function to create the 'main' window, where most of the information is
    def mainScreen(self):
        ##Modes are used to change between languages
        ##Mode 1 == English
        ##Mode 2 == Polish
        ##Mode 3 == Filipino
        mode = 1  
        if self.langchoice == "English":
            mode = 1
        elif self.langchoice == "Polska":
            mode = 2
        else:
            mode = 3

        self.mainScreen = QFrame()  ##Creates the main window
        self.mainScreen.setStyleSheet(self.styledata)

        self.instruct=QLabel("", self.mainScreen)  ##Shows instructions for user in certain modes
        self.instruct.setGeometry(QRect(300, 40, 200, 80))
        self.instruct.setObjectName("instruct")
        if mode == 2:
            self.instruct.setText("Proszę wybrać opcję")
        else:
            self.instruct.setText("")
            
        self.optLbl=QLabel("", self.mainScreen)  ##Shows labels for option buttons in certain mode 
        self.optLbl.setGeometry(QRect(30, 100, 150, 80))
        self.optLbl.setObjectName("optLbl")
        if mode == 2:
            self.optLbl.setText("OPCJE")
        else:
            self.optLbl.setText("")
        ############################################################################
        self.slogan=QLabel("", self.mainScreen)
        if mode == 2:
            self.slogan.setGeometry(QRect(30, 40, 200, 80))
        else:
            self.slogan.setGeometry(QRect(320, 40, 550, 80))
        self.slogan.setObjectName("slogan")

        self.pgLabel = QLabel("", self.mainScreen)  ##Shows the name home screen in different languages
        self.pgLabel.setGeometry(QRect(300, 10, 250, 45))
        self.pgLabel.setObjectName("pgLabel")

        self.flagicon=QIcon()

        self.infoBtn = QPushButton("", self.mainScreen)  ##Information buttons, shows more information
        if mode == 1:
            self.infoBtn.setGeometry(20, 100, 160, 50)
        else:
            self.infoBtn.setGeometry(20, 100, 160, 120)
        self.infoBtn.setToolTip('More Information')
        self.infoBtn.clicked.connect(self.infoScreen)
        if mode == 1:
            self.infoBtn.move(140, 100)
        elif mode == 2:
            self.infoBtn.move(20, 180)
        else:
            self.infoBtn.move(20, 100)

        self.ctBtn = QPushButton('Contact', self.mainScreen)  ##Contact buttons, shows contact information
        if mode == 1:
            self.ctBtn.setGeometry(20, 100, 160, 50)
        else:
            self.ctBtn.setGeometry(20, 100, 160, 120)
        self.ctBtn.setToolTip('Contact us')
        self.ctBtn.clicked.connect(self.contactScreen)
        if mode == 1:
            self.ctBtn.move(320, 100)
        elif mode == 2:
            self.ctBtn.move(20, 320)
        else:
            self.ctBtn.move(20, 240)

        self.lcBtn = QPushButton('Locations', self.mainScreen)  ##Location button, shows information re locations
        if mode == 1:
            self.lcBtn.setGeometry(20, 100, 160, 50)
        else:
            self.lcBtn.setGeometry(20, 100, 160, 120)
        self.lcBtn.setToolTip('Locations')
        self.lcBtn.clicked.connect(self.locationScreen)
        if mode == 1:
            self.lcBtn.move(500, 100)
        elif mode == 2:
            self.lcBtn.move(20, 460)
        else:
            self.lcBtn.move(20, 380)
            
        self.mainScreen.setFixedSize(800,600)
            
        self.info = QTextEdit("", self.mainScreen)  ##A read only text edit widge to display text from files
        self.info.setObjectName("info")
        if mode == 1:
           self.info.setGeometry(20,170,760,410)
        if (mode == 2) or (mode == 3):
           self.info.setGeometry(200,100,580,480)
        self.info.setReadOnly(True)
        
        mainScreentext=""  ##Empty 
        infoBtn=""
        ctBtn=""
        lcBtn=""
        pglbltext=""

        ##Code which opens files, and reads relevant text information, stores it in above empty variables
        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\detail.txt",'r') 
        for line in afile: 
             mainScreentext=mainScreentext+(str(line).rstrip('\n'))
        afile.close()

        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\infoBtn.txt",'r')
        for line in afile: 
             infoBtn=infoBtn+(str(line).rstrip('\n'))
        afile.close()

        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\ctBtn.txt",'r')
        for line in afile: 
             ctBtn=ctBtn+(str(line).rstrip('\n'))
        afile.close()

        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\lcBtn.txt",'r')
        for line in afile: 
             lcBtn=lcBtn+(str(line).rstrip('\n'))
        afile.close()

        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\pgLbl.txt",'r')
        for line in afile: 
             pglbltext=pglbltext+(str(line).rstrip('\n'))
        afile.close()
        
        self.info.setText(mainScreentext)  ##Sets text to text garnered from .txt files attained from above code
        self.infoBtn.setText(infoBtn)
        self.ctBtn.setText(ctBtn)
        self.lcBtn.setText(lcBtn)
        self.pgLabel.setText(pglbltext)

        locale.setlocale(locale.LC_ALL, self.locales[self.langs.index(self.langchoice)])

        self.mainScreen.setWindowTitle("Overseas Student Portal in "+self.langchoice)

        self.flagicon.addFile("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\flag.gif")
        self.mainScreen.setWindowIcon(self.flagicon)
        ################################################
        if mode == 1:
            self.slogan.setText('For only ' + locale.currency(1255.90, grouping = True) + '!')
        if mode == 2:
            self.slogan.setText('Tylko dla ' + locale.currency(1255.90, grouping = True) + '!')
        if mode == 3:
            self.slogan.setText('Para lamang ' + locale.currency(1255.90, grouping = True) + '!')

        self.mainScreen.show()

    def infoScreen(self):  ##Window which opens when information buttons is pressed
        infotext=""
        self.infoS = QFrame() 
        self.infoS.setStyleSheet(self.styledata)
        self.infoS.setFixedSize(500,500)

        self.infoSTE = QTextEdit("", self.infoS)
        self.infoSTE.setGeometry(20,20,460,460)
        self.infoSTE.setReadOnly(True)


        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\infoTxt.txt",'r') 
        for line in afile: 
             infotext=infotext+(str(line).rstrip('\n'))
        afile.close()

        self.infoSTE.setText(infotext)
        
        self.infoS.show()

    def contactScreen(self):  ##Window which opens when contact buttons is pressed
        contacttext=""
        self.ctS = QFrame() 
        self.ctS.setStyleSheet(self.styledata)
        self.ctS.setFixedSize(500,500)

        self.ctSTE = QTextEdit("", self.ctS)
        self.ctSTE.setGeometry(20,20,460,460)
        self.ctSTE.setReadOnly(True)

        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\ctTxt.txt",'r') 
        for line in afile: 
             contacttext=contacttext+(str(line).rstrip('\n'))
        afile.close()

        self.ctSTE.setText(contacttext)
        
        self.ctS.show()

    def locationScreen(self):  ##Window which opens when location buttons is pressed
        locationtext=""
        self.locS = QFrame()
        self.locS.setStyleSheet(self.styledata)
        self.locS.setFixedSize(500,500)

        self.locSTE = QTextEdit("", self.locS)
        self.locSTE.setGeometry(20,20,460,460)
        self.locSTE.setReadOnly(True)


        afile=open("resources\\"+self.rfolders[self.langs.index(self.langchoice)]+"\\lcTxt.txt",'r') 
        for line in afile: 
             locationtext=locationtext+(str(line).rstrip('\n'))
        afile.close()

        self.locSTE.setText(locationtext)
        
        self.locS.show()

    ##Checks to see if radio button on entry screen has been checked, if it has, it's text is set to 'langchoice'   
    def langButtonCheck(self, btn):
        if btn.isChecked() == True:
            self.langchoice=btn.text()
            f = open('tracker.txt', 'w')
            f.write("%s\n" % self.langchoice)
            f.close()

    ##connected to buttons which exits interface, function just exits down interface      
    def exitBtn(self):
        QCoreApplication.instance().quit()
        sys.exit()

def main():
    app = QApplication(sys.argv)
    appform = portal()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

