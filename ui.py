#!/usr/bin/python


import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()
    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setToolTip('This is <b>QWidget</b> widget')

        btn=QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)


        menubar=self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)


        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.setWindowIcon(QtGui.QIcon('image/marisa_small.gif'))
        self.show()

        exitAction = QtGui.QAction(QtGui.QIcon('image/marisa_small.gif'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)



    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, "Message", "Are you sure to quit?", QtGui.QMessageBox.Yes | \
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app=QtGui.QApplication(sys.argv)
    ex=Example()

    sys.exit(app.exec_())

if __name__=='__main__':
    main()