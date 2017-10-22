import sys
from PyQt4 import QtGui, QtCore
from time import strftime #we have to import strftime from the time module 

var = True

class Main(QtGui.QMainWindow):
        def _init_(self):
                QtGui.QmaniWIndow._init_(self)
                self.initUI()

        def initUI(self):

                timer = QtCOre.QTimer(self)
                timer.timeout.connect(self.Time)
                timer.start(10) #update time in seconds

                self.lcd = QtGui.QLCDNumber(self)
                self.lcd.resize(250,100)
                self.lcd.move(0,30)
                self.lcd.display(strftime("%H"+":"+"%M"))

                self.r1 = QtGui.QRadioButton("Hide seconds", self)
                self.r1.move(10,0)
                self.r2 = QtGui.QRadioButton("Show seconds", self)
                self.r2.move(110,0)

                self.r1.toggled.connect(self.woSecs)
                self.r2.toggled.connect(self.wSecs)

                self.setGeometry(300,300,250,130)
                self.setWindowTitle("Clock")
                self.setWindowIcon(QtGui.QIcon(""))
                self.show()


        def Time(self):
                global var

                if var == True:
                        self.lcd.display(strftime("%H"+":"+"%M"))
                elif var == False:
                        self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))


        def wSecs(self):
            global var
            var = False

            self.resize(375,130)
            self.lcd.resize(375,100)
            self.lcd.setDigitCount(8)

        def woSecs(self):
                global var
                var = True

                self.resize(250,130)
                self.lcd.resize(250,100)
                self.lcd.setDigitCount(5)

        def main():
                app = QtGui.QApplication(sys.argv)
                main = Main()
                main.show()

                sys.exit(app.exec_())


        if _name_ == "_main_":
                main()

            
        
                
