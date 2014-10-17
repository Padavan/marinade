#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
    def initUI(self):


        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is <b>QWidget</b> widget')

        #self.resize(400,400)
        self.centralwidget = QtGui.QWidget(self)

        self.btn=QtGui.QPushButton('Button', self.centralwidget)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.resize(self.btn.sizeHint())

        self.timeText = QtGui.QLabel(self.centralwidget)
        #self.timeText.setText("00:00")
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.display("00:00")

        self.vbox=QtGui.QVBoxLayout(self.centralwidget)
        self.vbox.addWidget(self.lcdNumber)
        self.vbox.addWidget(self.btn)
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
        self.aboutWindowStart.show()

class AboutWindow(QtGui.QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.initUI()

    def initUI(self):
        app = QtGui.QMainWindow()

        w = QtGui.QWidget()
        w.resize(250, 150)
        w.move(300, 300)
        w.setWindowTitle('Simple')
        w.show()





"""
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, "Message", "Are you sure to quit?", QtGui.QMessageBox.Yes | \
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
"""

def main():
    app=QtGui.QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
