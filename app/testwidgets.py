<<<<<<< HEAD
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
=======
#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import ConfigParser


class PrefWindow(QtGui.QWidget):
    def __init__(self):
        super(PrefWindow, self).__init__()
        self.initUI()

        #self.rest=self.ex.rest()
        #self.lrest=self.ex.lrest()


    def initUI(self):
        self.mainWidget = QtGui.QWidget(parent=None)
        self.tabWidget = QtGui.QTabWidget(self.mainWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 391, 271))
        self.tab1=QtGui.QWidget()

#--------Tab 1-----------------------------------------------------------------
 #-------смотреть здесь------------
        self.ex=Config()
        #self.ex.write()
        self.ex.read()

        self.label1=QtGui.QLabel("Pomodoro Time", self.tab1)
        self.slider1=QtGui.QSlider(QtCore.Qt.Horizontal, self.tab1)
        self.sbox1=QtGui.QSpinBox(self.tab1)
        self.slider1.setValue(self.ex.pomodoro)
        self.sbox1.setValue(self.ex.pomodoro)
        self.slider1.valueChanged.connect(self.sbox1.setValue)
        self.sbox1.valueChanged.connect(self.slider1.setValue)
#-------/смотреть здесь------------
        self.hbox1=QtGui.QHBoxLayout()
        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.slider1)
        self.hbox1.addWidget(self.sbox1)

        self.label2=QtGui.QLabel("Rest", self.tab1)
        self.slider2=QtGui.QSlider(QtCore.Qt.Horizontal, self.tab1)
        self.sbox2=QtGui.QSpinBox(self.tab1)
        self.slider2.setValue(self.ex.rest)
        self.sbox2.setValue(self.ex.rest)
        self.slider2.valueChanged.connect(self.sbox2.setValue)
        self.sbox2.valueChanged.connect(self.slider2.setValue)
        self.hbox2=QtGui.QHBoxLayout()
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.slider2)
        self.hbox2.addWidget(self.sbox2)

        self.label3=QtGui.QLabel("Long Rest", self.tab1)
        self.slider3=QtGui.QSlider(QtCore.Qt.Horizontal, self.tab1)
        self.sbox3=QtGui.QSpinBox(self.tab1)
        self.slider3.setValue(self.ex.lrest)
        self.sbox3.setValue(self.ex.lrest)
        self.slider3.valueChanged.connect(self.sbox3.setValue)
        self.sbox3.valueChanged.connect(self.slider3.setValue)
        self.hbox3=QtGui.QHBoxLayout()
        self.hbox3.addWidget(self.label3)
        self.hbox3.addWidget(self.slider3)
        self.hbox3.addWidget(self.sbox3)

        self.chbox4=QtGui.QCheckBox('Ticking Sound')
        self.chbox4.setChecked(self.ex.sound)
        #print self.chbox4.isChecked()
        #self.label4=QtGui.QLabel("Ticking Sound")
        #self.hbox4=QtGui.QHBoxLayout()
        #self.hbox4.addWidget(self.chbox4)
        #self.hbox4.addWidget(self.label4)

        self.bigVBox=QtGui.QVBoxLayout()
        self.bigVBox.addLayout(self.hbox1)
        self.bigVBox.addLayout(self.hbox2)
        self.bigVBox.addLayout(self.hbox3)
        self.bigVBox.addWidget(self.chbox4)
        self.tab1.setLayout(self.bigVBox)


#--------Tab 2-----------------------------------------------------------------
        self.tab2=QtGui.QWidget()

#--------Widget settings-----------------------------------------------------------------
        self.tabWidget.addTab(self.tab1, "Timer")
        self.tabWidget.addTab(self.tab2, "Notification")



        self.saveButton=QtGui.QPushButton('Save', self.mainWidget)
        self.saveButton.clicked.connect(self.printValues)
        self.cancelButton=QtGui.QPushButton('Cancel', self.mainWidget)
        self.bottomHBox=QtGui.QHBoxLayout()
        self.bottomHBox.addStretch()
        self.bottomHBox.addWidget(self.saveButton)
        self.bottomHBox.addWidget(self.cancelButton)

        self.mainVBox=QtGui.QVBoxLayout()
        self.mainVBox.addWidget(self.tabWidget)
        self.mainVBox.addLayout(self.bottomHBox)
        self.mainWidget.setLayout(self.mainVBox)



        self.mainWidget.resize(400, 400)
        self.mainWidget.setWindowTitle('Preferences')
        self.mainWidget.setWindowIcon(QtGui.QIcon('image/marisa_small.gif'))
        self.mainWidget.show()
#-------эта штука для проверки значений------------
    def printValues(self):
        self.ex.pomodoro = self.slider1.value()
        self.ex.rest = self.slider2.value()
        self.ex.lrest = self.slider3.value()
        self.ex.sound = self.chbox4.isChecked()
        print self.ex.pomodoro, self.ex.rest, self.ex.lrest
        print self.ex.sound
        self.ex.write()
#-----здесь будет ex.write()


"""
    this class for interaction with config file.
    it based on ConfigParser module
    from standard library
"""
class Config(object):

    def __init__(self):
        self.config=ConfigParser.ConfigParser()
        self.pomodoro = 0
        self.rest = 0
        self.lrest = 0

    def read(self):
        #self.cfgfile=open('config.ini')
        self.config.read('config.ini')
        #print self.config.sections()
        self.pomodoro=self.config.getint('Timer', 'Pomodoro')
        #print "configvalue %d" % self.pomodoro
        self.rest=self.config.getint('Timer', 'Rest')
        self.lrest=self.config.getint('Timer', 'Long Rest')
        self.sound=self.config.getboolean('Timer', 'sound')
        print self.sound
        #self.cfgfile.close()
    def write(self):

        self.cfgfile=open('config.ini', 'w')

        #self.config.add_section('Timer')
        self.config.set('Timer', 'Pomodoro', self.pomodoro)
        self.config.set('Timer', 'Rest', self.rest)
        self.config.set('Timer', 'Long Rest', self.lrest)
        self.config.set('Timer', 'sound', self.sound)

        self.config.write(self.cfgfile)
        self.cfgfile.close()
    def update(self):
        pass

def main():
    app=QtGui.QApplication(sys.argv)
    ex=PrefWindow()
    sys.exit(app.exec_())

if __name__=='__main__':
>>>>>>> f85633c86d99f9bef1ec0634728cbf7cdbfc08f9
    main()