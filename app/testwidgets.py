#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import ConfigParser


class PrefWindow(QtGui.QWidget):
    def __init__(self):
        super(PrefWindow, self).__init__()
        self.initUI()
        self.ex=Config()
        self.ex.read()
        self.pomodoro=self.ex.pomodoro
        #self.rest=self.ex.rest()
        #self.lrest=self.ex.lrest()


    def initUI(self):
        self.mainWidget = QtGui.QWidget(parent=None)
        self.tabWidget = QtGui.QTabWidget(self.mainWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 391, 271))
        self.tab1=QtGui.QWidget()

#--------Tab 1-----------------------------------------------------------------


        self.label1=QtGui.QLabel("Pomodoro Time", self.tab1)
        self.slider1=QtGui.QSlider(QtCore.Qt.Horizontal, self.tab1)
        self.sbox1=QtGui.QSpinBox(self.tab1)
        self.slider1.valueChanged.connect(self.sbox1.setValue)
        self.sbox1.valueChanged.connect(self.slider1.setValue)

        self.hbox1=QtGui.QHBoxLayout()
        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.slider1)
        self.hbox1.addWidget(self.sbox1)

        self.label2=QtGui.QLabel("Rest", self.tab1)
        self.slider2=QtGui.QSlider(QtCore.Qt.Horizontal, self.tab1)
        self.sbox2=QtGui.QSpinBox(self.tab1)
        self.slider2.valueChanged.connect(self.sbox2.setValue)
        self.sbox2.valueChanged.connect(self.slider2.setValue)
        self.hbox2=QtGui.QHBoxLayout()
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.slider2)
        self.hbox2.addWidget(self.sbox2)

        self.label3=QtGui.QLabel("Long Rest", self.tab1)
        self.slider3=QtGui.QSlider(QtCore.Qt.Horizontal, self.tab1)
        self.sbox3=QtGui.QSpinBox(self.tab1)
        self.slider3.valueChanged.connect(self.sbox3.setValue)
        self.sbox3.valueChanged.connect(self.slider3.setValue)
        self.hbox3=QtGui.QHBoxLayout()
        self.hbox3.addWidget(self.label3)
        self.hbox3.addWidget(self.slider3)
        self.hbox3.addWidget(self.sbox3)

        self.chbox4=QtGui.QCheckBox()
        self.label4=QtGui.QLabel("Ticking Sound")
        self.hbox4=QtGui.QHBoxLayout()
        self.hbox4.addWidget(self.chbox4)
        self.hbox4.addWidget(self.label4)

        self.bigVBox=QtGui.QVBoxLayout()
        self.bigVBox.addLayout(self.hbox1)
        self.bigVBox.addLayout(self.hbox2)
        self.bigVBox.addLayout(self.hbox3)
        self.bigVBox.addLayout(self.hbox4)
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

    def printValues(self):
        self.pomodoro = self.slider1.value()
        print self.pomodoro


"""
    this class for interaction with config file.
    it based on ConfigParser module
    from standard library
"""
class Config(object):

    def __init__(self):
        self.config=ConfigParser.ConfigParser()

    def read(self):
        #self.cfgfile=open('config.ini')
        self.config.read('config.ini')
        print self.config.sections()
        self.pomodoro=self.config.getint('Timer', 'Pomodoro')
        print "configvalue %d" % self.pomodoro
        self.rest=self.config.getint('Timer', 'Rest')
        self.lrest=self.config.getint('Timer', 'Long Rest')
        #self.cfgfile.close()
    def write(self):
        self.cfgfile=open('config.ini', 'w')

        self.config.set('Timer', 'Pomodoro', self.pomodoro)
        self.config.set('Timer', 'Rest', self.rest)
        self.config.set('Timer', 'Long Rest', self.lrest)

        self.config.write(cfgfile)
        self.cfgfile.close()
    def update(self):
        pass

def main():
    app=QtGui.QApplication(sys.argv)
    ex=PrefWindow()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()