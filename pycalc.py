# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_calc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
       
        self.screen = QtWidgets.QLineEdit(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(52, 30, 471, 51))
        self.screen.setObjectName("screen")

        self.lcdEqual = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdEqual.setGeometry(QtCore.QRect(200, 90, 321, 81))
        self.lcdEqual.setObjectName("lcdEqual")
       
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setGeometry(QtCore.QRect(60, 210, 93, 28))
        self.pb1.setObjectName("pb1")
        self.pb1.clicked.connect(lambda: self.changeScr('1'))

        self.pb7 = QtWidgets.QPushButton(self.centralwidget)
        self.pb7.setGeometry(QtCore.QRect(60, 310, 93, 28))
        self.pb7.setObjectName("pb7")
        self.pb7.clicked.connect(lambda: self.changeScr('7'))
       
        self.pb5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb5.setGeometry(QtCore.QRect(180, 260, 93, 28))
        self.pb5.setObjectName("pb5")
        self.pb5.clicked.connect(lambda: self.changeScr('5'))
       
        self.pb4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb4.setGeometry(QtCore.QRect(60, 260, 93, 28))
        self.pb4.setObjectName("pb4")
        self.pb4.clicked.connect(lambda: self.changeScr('4'))
       
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setGeometry(QtCore.QRect(180, 210, 93, 28))
        self.pb2.setObjectName("pb2")
        self.pb2.clicked.connect(lambda: self.changeScr('2'))
       
        self.pb8 = QtWidgets.QPushButton(self.centralwidget)
        self.pb8.setGeometry(QtCore.QRect(180, 310, 93, 28))
        self.pb8.setObjectName("pb8")
        self.pb8.clicked.connect(lambda: self.changeScr('8'))
       
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setGeometry(QtCore.QRect(300, 210, 93, 28))
        self.pb3.setObjectName("pb3")
        self.pb3.clicked.connect(lambda: self.updatelcd(self.lcd1,3))
       
        self.pb9 = QtWidgets.QPushButton(self.centralwidget)
        self.pb9.setGeometry(QtCore.QRect(300, 310, 93, 28))
        self.pb9.setObjectName("pb9")
        self.pb9.clicked.connect(lambda: self.updatelcd(self.lcd1,9))
       
        self.pb6 = QtWidgets.QPushButton(self.centralwidget)
        self.pb6.setGeometry(QtCore.QRect(300, 260, 93, 28))
        self.pb6.setObjectName("pb6")
        self.pb6.clicked.connect(lambda: self.updatelcd(self.lcd1,6))
       
        self.pbmius = QtWidgets.QPushButton(self.centralwidget)
        self.pbmius.setGeometry(QtCore.QRect(440, 260, 93, 28))
        self.pbmius.setObjectName("pbmius")
        self.pbmius.clicked.connect(lambda: self.updatelcd(self.lcd1,'-'))
       
        self.pbplus = QtWidgets.QPushButton(self.centralwidget)
        self.pbplus.setGeometry(QtCore.QRect(440, 210, 93, 28))
        self.pbplus.setObjectName("pbplus")
        self.pbplus.clicked.connect(lambda: self.updatelcd(self.lcd1,'+'))
       
        self.pbequal = QtWidgets.QPushButton(self.centralwidget)
        self.pbequal.setGeometry(QtCore.QRect(440, 310, 93, 28))
        self.pbequal.setObjectName("pbequal")
        self.pbequal.clicked.connect(lambda: self.updatelcd(self.lcd1,"="))
       
        self.pb0 = QtWidgets.QPushButton(self.centralwidget)
        self.pb0.setGeometry(QtCore.QRect(180, 360, 93, 28))
        self.pb0.setObjectName("pb0")
        self.pb0.clicked.connect(lambda: self.updatelcd(self.lcd1,0))
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
       
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
       
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def updatelcd(self,num):
        self.num = num
        self.lcd.display(self.num)

    def changeScr(self,text):
        self.text = "text"
        self.screen.setText(self.text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb1.setText(_translate("MainWindow", "1"))
        self.pb7.setText(_translate("MainWindow", "7"))
        self.pb5.setText(_translate("MainWindow", "5"))
        self.pb4.setText(_translate("MainWindow", "4"))
        self.pb2.setText(_translate("MainWindow", "2"))
        self.pb8.setText(_translate("MainWindow", "8"))
        self.pb3.setText(_translate("MainWindow", "3"))
        self.pb9.setText(_translate("MainWindow", "9"))
        self.pb6.setText(_translate("MainWindow", "6"))
        self.pbmius.setText(_translate("MainWindow", "-"))
        self.pbplus.setText(_translate("MainWindow", "+"))
        self.pbequal.setText(_translate("MainWindow", "="))
        self.pb0.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
