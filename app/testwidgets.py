from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
import sys

class myLCDNumber(QtGui.QLCDNumber):
  value = 60
    
  @pyqtSlot()
  def count(self):
    self.display(self.value)
    self.value = self.value-1


def main():    
    app 	 = QtGui.QApplication(sys.argv)
    lcdNumber	 = myLCDNumber()

    #Resize width and height
    lcdNumber.resize(250,250)    
    lcdNumber.setWindowTitle('PyQt QLcdNumber Countdown Example')  
    
    timer = QtCore.QTimer()
    lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("count()"))
    timer.start(1000) 

    lcdNumber.show()    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()