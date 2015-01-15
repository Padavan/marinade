#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot,SIGNAL,SLOT
<<<<<<< HEAD
import time
=======
import time,threading
>>>>>>> f85633c86d99f9bef1ec0634728cbf7cdbfc08f9

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    def initUI(self):


        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is <b>QWidget</b> widget')

        #self.resize(400,400)
        self.centralwidget = QtGui.QWidget(self)
#----------------------------------------------------------

        self.tmr=Timer()

        self.btn=QtGui.QPushButton('Start', self.centralwidget)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.toggle)


<<<<<<< HEAD
        self.now=0
=======
>>>>>>> f85633c86d99f9bef1ec0634728cbf7cdbfc08f9
        #self.timeText = QtGui.QLabel(self.centralwidget)
        #self.timeText.setText("00:00")

        self.timer=QtCore.QTimer()
<<<<<<< HEAD
        self.value=60
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.display(60)
        self.lcdNumber.connect(self.timer,SIGNAL("timeout()"),self.lcdNumber,SLOT("count()"))


        self.timer.start(100)

        #"%02d:%02d" % divmod(self.now, 60)



=======
        self.timer.timeout.connect(self.countdown)
        #self.timer.start(1000)
        self.e=threading.Thread(target=self.timer.start(1000))
        self.e.start()
        #self.thread = QtCore.QThread()
        #self.thread.timer.start(100)

        #self.value=60
        self.now=self.tmr.dumb()
        #self.timer2=threading.Thread(target=self.tmr.start)

        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.display(self.now)
        #self.lcdNumber.connect(self.timer, SIGNAL(timeout()), self, SLOT(update()))

        #self.lcdNumber.connect(self.timer,SIGNAL("timeout()"),self.lcdNumber,SLOT("count()"))
#----------------------------------------------------------
        #"%02d:%02d" % divmod(self.now, 60)
        self.hbox=QtGui.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.btn)
        self.hbox.addStretch(1)
>>>>>>> f85633c86d99f9bef1ec0634728cbf7cdbfc08f9

        self.vbox=QtGui.QVBoxLayout(self.centralwidget)
        self.vbox.addWidget(self.lcdNumber)
        self.vbox.addLayout(self.hbox)
        self.setCentralWidget(self.centralwidget)


        #qbtn = QtGui.QPushButton('Quit', self)
        #         #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #qbtn.resize(qbtn.sizeHint())
        #qbtn.move(50, 100)

        #self.vbox = QtGui.QVBoxLayout()
        #self.vbox.addWidget(self.timeText)
        #self.vbox.addWidget(self.btn)

        #self.setLayout(self.vbox)

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)


        #menubar=self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(exitAction)


        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.setWindowIcon(QtGui.QIcon('image/marisa_small.gif'))
        self.show()
##------------------------------------------------TOOLBAR-------------------------------




        self.menu = QtGui.QMenu()

        self.startAction = QtGui.QAction("Start", self)
        self.menu.addAction(self.startAction)
        self.startAction.setShortcut('Ctrl+S')
        self.startAction.triggered.connect(self.dummy)

        self.stopAction = QtGui.QAction("Stop", self)
        self.menu.addAction(self.stopAction)

        self.optAction = QtGui.QAction("Preference", self)
        self.menu.addAction(self.optAction)
        self.optAction.triggered.connect(self.callPreferences)

        #self.aboutWindowStart=AboutWindow()
        self.aboutAction = QtGui.QAction("About", self)
        self.menu.addAction(self.aboutAction)
        self.aboutAction.triggered.connect(self.callWindow)

        self.closeAction = QtGui.QAction("Quit", self)
        self.menu.addAction(self.closeAction)
        self.closeAction.setShortcut('Ctrl+Q')
        self.closeAction.triggered.connect(QtGui.qApp.quit)


        self.left_spacer = QtGui.QWidget()
        self.left_spacer.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        self.tool_button = QtGui.QToolButton()
        self.tool_button.setMenu(self.menu)
        self.tool_button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.tool_button.setToolTip("shittooltip")
        self.tool_button.setFixedWidth(50)
        self.tool_button.setIcon(QtGui.QIcon('image/gears.svg'))


        self.tool_button_action = QtGui.QWidgetAction(self)
        self.tool_button_action.setDefaultWidget(self.tool_button)


        #exitAction = QtGui.QAction(QtGui.QIcon('image/marisa_small.gif'), 'Exit', self)
        #exitAction.setShortcut('Ctrl+Q')
        #exitAction.triggered.connect(QtGui.qApp.quit)
        #exitAction.triggered.connect()

        self.toolbar = self.addToolBar('Shit')
        self.toolbar.addWidget(self.left_spacer)
        self.toolbar.addAction(self.tool_button_action)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Marinade')
        self.show()

    def dummy(self):
        print "dummy fun"

    def callWindow(self):
        print "callWindow method call"
        self.aboutWindowStart=AboutWindow()
        #self.aboutWindowStart.show()
    def count(self):
        self.display(self.value)
        self.value = self.value-1

    def callPreferences(self):
        print "call preference method"
        self.prefWindowStart=PrefWindow()

    def countdown(self):
        self.now=self.tmr.dumb()
        print "countdoun %d" % self.now
        #self.now2="%02d:%02d" % divmod(self.now, 60)
        self.lcdNumber.display("%02d:%02d" % divmod(self.now, 60))

    def toggle(self):
        sender=self.sender()
        if self.btn.text()=="Start":
            self.statusBar().showMessage(sender.text() + ' was pressed')
            self.btn.setText("Stop")
            #self.tmr.start()

            self.w=threading.Thread(target=self.tmr.start)
            self.w.start()
        else:
            self.statusBar().showMessage(sender.text() + ' was pressed')
            self.btn.setText("Start")
            self.tmr.stop()

class AboutWindow(QtGui.QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.initUI()

    def initUI(self):


        self.mainWidget = QtGui.QWidget(parent=None)


        self.nameLabel = QtGui.QLabel('marinade', self.mainWidget)
        self.nameLabel.setText("Marinade")
        self.nameLabel.setFont(QtGui.QFont('SansSerif', 14))
        #self.nameLabel.setAlignment(QtCore.Qt.AlignLeft)

        self.versionLabel = QtGui.QLabel(self.mainWidget)
        self.versionLabel.setText("Version 0.1")

        self.pictureLabel = QtGui.QLabel(self.mainWidget)
        self.pictureLabel.setPixmap(QtGui.QPixmap("image/marisa_small.gif"))

        self.grid=QtGui.QGridLayout()
        self.grid.setSpacing(10)
        self.grid.addWidget(self.nameLabel, 0, 1, 0, 2 )
        self.grid.addWidget(self.versionLabel, 1, 1, 1, 2)
        self.grid.addWidget(self.pictureLabel, 0, 0, 0, 1)






        self.group = QtGui.QGroupBox(self.mainWidget)
        self.group.setTitle("MIT Public License")
        self.license = QtGui.QTextEdit(self.group)

        self.text=open('LICENSE').read()
        self.license.setPlainText(self.text)
        self.license.setReadOnly(True)




        self.okbutton = QtGui.QPushButton("OK", self.mainWidget)
        self.okbutton.clicked.connect(self.mainWidget.close)
        self.hbox2=QtGui.QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.okbutton)


        self.vbox2=QtGui.QVBoxLayout()
        self.vbox2.addWidget(self.license)
        self.group.setLayout(self.vbox2)




        self.vbox=QtGui.QVBoxLayout()
        self.vbox.addLayout(self.grid)
        self.vbox.addWidget(self.group)
        self.vbox.addLayout(self.hbox2)

        self.mainWidget.setLayout(self.vbox)


        self.mainWidget.resize(400, 400)
        self.mainWidget.setWindowTitle('About')
        self.mainWidget.setWindowIcon(QtGui.QIcon('image/marisa_small.gif'))
        self.mainWidget.show()

    #def okClicked(self):
        #print "ok clicked"
        #self.mainWidget.close()
<<<<<<< HEAD
=======


class Timer(object):
    def __init__(self):
        object.__init__(self)
        self.minutes=5
        self.count=self.minutes*1
        self.is_state=False
    def start(self):
        self.is_state=False
        while self.count > 0:
            self.count-=1
            time.sleep(1)
            print self.is_state
            print self.count
            if self.is_state:
                break
    def stop(self):
        self.minutes=5
        self.count=5
        self.is_state=True
    def dumb(self):
        return self.count

class PrefWindow(QtGui.QWidget):
    def __init__(self):
        super(PrefWindow, self).__init__()
        self.initUI()
>>>>>>> f85633c86d99f9bef1ec0634728cbf7cdbfc08f9

    def initUI(self):
        self.mainWidget = QtGui.QWidget(parent=None)



        self.mainWidget.resize(400, 400)
        self.mainWidget.setWindowTitle('Preferences')
        self.mainWidget.setWindowIcon(QtGui.QIcon('image/marisa_small.gif'))
        self.mainWidget.show()

def main():
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
