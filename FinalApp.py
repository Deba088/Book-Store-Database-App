# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.gridLayout.addWidget(self.t1, 1, 1, 1, 1)
        self.l3 = QtWidgets.QLabel(Form)
        self.l3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l3.setObjectName("l3")
        self.gridLayout.addWidget(self.l3, 4, 0, 1, 1)
        self.l1 = QtWidgets.QLabel(Form)
        self.l1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l1.setObjectName("l1")
        self.gridLayout.addWidget(self.l1, 1, 0, 1, 1)
        self.l2 = QtWidgets.QLabel(Form)
        self.l2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.l2.setObjectName("l2")
        self.gridLayout.addWidget(self.l2, 3, 0, 1, 1)
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setObjectName("t3")
        self.gridLayout.addWidget(self.t3, 4, 1, 1, 1)
        self.l4 = QtWidgets.QLabel(Form)
        self.l4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.l4.setObjectName("l4")
        self.gridLayout.addWidget(self.l4, 5, 0, 1, 1)
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 1, 2, 1, 1)
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 4, 2, 1, 1)
        self.l5 = QtWidgets.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l5.setPalette(palette)
        self.l5.setText("")
        self.l5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.l5.setObjectName("l5")
        self.gridLayout.addWidget(self.l5, 3, 1, 1, 1)
        self.l6 = QtWidgets.QLabel(Form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.l6.setPalette(palette)
        self.l6.setText("")
        self.l6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.l6.setObjectName("l6")
        self.gridLayout.addWidget(self.l6, 5, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.t3.setValidator(QtGui.QIntValidator())
        self.b1.clicked.connect(self.findprice)
        self.b2.clicked.connect(self.total)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l3.setText(_translate("Form", "Quantity :"))
        self.l1.setText(_translate("Form", "Book Title :"))
        self.l2.setText(_translate("Form", "Price :"))
        self.l4.setText(_translate("Form", "Total :"))
        self.b1.setText(_translate("Form", "Find Price"))
        self.b2.setText(_translate("Form", "Find Total"))

    def findprice(self, Form):
        _translate = QtCore.QCoreApplication.translate
        txt = self.t1.text()
        BookStore = sqlite3.connect("BookStores.db")
        cursbook = BookStore.cursor()
        cursbook.execute("SELECT Name, Price FROM Book WHERE Name == '" + txt + "';")
        record = cursbook.fetchone()
        if record[0] != self.t1.text():
            self.l5.setText(_translate("Form", "This book is not available"))
        else:
            self.l5.setText(_translate("Form", "Rs. " + str(record[1])))
        BookStore.commit()

    def total(self, Form):
        _translate = QtCore.QCoreApplication.translate
        txt = self.t3.text()
        txt1 = self.l5.text()
        txt2 = txt1.split(" ")
        total = int(txt) * int(txt2[1])
        self.l6.setText(_translate("Form", "Rs. "+str(total)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

