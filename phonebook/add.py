# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from fun import addStudent

class Ui_addDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setObjectName("addDialog")
        self.resize(310, 535)
        self.setMinimumSize(QtCore.QSize(310, 535))
        self.setMaximumSize(QtCore.QSize(310, 535))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.confirmButton = QtWidgets.QPushButton(self)
        self.confirmButton.setGeometry(QtCore.QRect(50, 490, 93, 28))
        self.confirmButton.setAutoDefault(True)
        self.confirmButton.setObjectName("confirmButton")
        self.cancleButton = QtWidgets.QPushButton(self)
        self.cancleButton.setGeometry(QtCore.QRect(170, 490, 93, 28))
        self.cancleButton.setObjectName("cancleButton")
        self.radioButton_man = QtWidgets.QRadioButton(self)
        self.radioButton_man.setGeometry(QtCore.QRect(130, 140, 51, 19))
        self.radioButton_man.setObjectName("radioButton_man")
        self.radioButton_man.setChecked(True)
        self.radioButton_women = QtWidgets.QRadioButton(self)
        self.radioButton_women.setGeometry(QtCore.QRect(200, 140, 51, 19))
        self.radioButton_women.setObjectName("radioButton_women")
        self.idlabel = QtWidgets.QLabel(self)
        self.idlabel.setGeometry(QtCore.QRect(50, 40, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName("idlabel")
        self.namelabel = QtWidgets.QLabel(self)
        self.namelabel.setGeometry(QtCore.QRect(50, 90, 41, 16))
        self.namelabel.setObjectName("namelabel")
        self.sexlabe = QtWidgets.QLabel(self)
        self.sexlabe.setGeometry(QtCore.QRect(50, 140, 41, 16))
        self.sexlabe.setObjectName("sexlabe")
        self.agelabel = QtWidgets.QLabel(self)
        self.agelabel.setGeometry(QtCore.QRect(50, 190, 41, 16))
        self.agelabel.setObjectName("agelabel")
        self.bornlabel = QtWidgets.QLabel(self)
        self.bornlabel.setGeometry(QtCore.QRect(50, 240, 72, 15))
        self.bornlabel.setObjectName("bornlabel")
        self.phonelabel = QtWidgets.QLabel(self)
        self.phonelabel.setGeometry(QtCore.QRect(50, 290, 72, 15))
        self.phonelabel.setObjectName("phonelabel")
        self.emaillabel = QtWidgets.QLabel(self)
        self.emaillabel.setGeometry(QtCore.QRect(50, 340, 72, 15))
        self.emaillabel.setObjectName("emaillabel")
        self.homelabel = QtWidgets.QLabel(self)
        self.homelabel.setGeometry(QtCore.QRect(50, 390, 72, 15))
        self.homelabel.setObjectName("homelabel")
        self.professlabel = QtWidgets.QLabel(self)
        self.professlabel.setGeometry(QtCore.QRect(50, 440, 41, 16))
        self.professlabel.setObjectName("professlabel")
        self.idlineEdit = QtWidgets.QLineEdit(self)
        self.idlineEdit.setGeometry(QtCore.QRect(130, 40, 131, 21))
        self.idlineEdit.setObjectName("idlineEdit")
        self.namelineEdit = QtWidgets.QLineEdit(self)
        self.namelineEdit.setGeometry(QtCore.QRect(130, 90, 131, 21))
        self.namelineEdit.setObjectName("namelineEdit")
        self.borndateEdit = QtWidgets.QDateEdit(self)
        self.borndateEdit.setGeometry(QtCore.QRect(130, 240, 121, 22))
        self.borndateEdit.setObjectName("borndateEdit")
        self.phonelineEdit = QtWidgets.QLineEdit(self)
        self.phonelineEdit.setGeometry(QtCore.QRect(130, 290, 131, 21))
        self.phonelineEdit.setObjectName("phonelineEdit")
        self.emaillineEdit = QtWidgets.QLineEdit(self)
        self.emaillineEdit.setGeometry(QtCore.QRect(130, 340, 131, 21))
        self.emaillineEdit.setObjectName("emaillineEdit")
        self.homelineEdit = QtWidgets.QLineEdit(self)
        self.homelineEdit.setGeometry(QtCore.QRect(130, 390, 131, 21))
        self.homelineEdit.setObjectName("homelineEdit")
        self.agespinBox = QtWidgets.QSpinBox(self)
        self.agespinBox.setGeometry(QtCore.QRect(130, 190, 71, 22))
        self.agespinBox.setObjectName("agespinBox")
        self.professcomboBox = QtWidgets.QComboBox(self)
        self.professcomboBox.setGeometry(QtCore.QRect(130, 440, 131, 22))
        self.professcomboBox.setObjectName("professcomboBox")
        self.professcomboBox.addItem("")
        self.professcomboBox.addItem("")
        self.professcomboBox.addItem("")
        self.professcomboBox.addItem("")

        self.retranslateUi()
        self.cancleButton.clicked['bool'].connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.confirmButton.clicked.connect(lambda: addStudent(
            self.idlineEdit.text(),
            self.namelineEdit.text(),
            self.radioButton_man,
            self.radioButton_women,
            self.agespinBox.value(),
            self.borndateEdit.text(),
            self.phonelineEdit.text(),
            self.emaillineEdit.text(),
            self.homelineEdit.text(),
            self.professcomboBox.currentText(),
            self
        ))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("addDialog", "添加学生信息"))
        self.confirmButton.setText(_translate("addDialog", "添加"))
        self.cancleButton.setText(_translate("addDialog", "取消"))
        self.radioButton_man.setText(_translate("addDialog", "男"))
        self.radioButton_women.setText(_translate("addDialog", "女"))
        self.idlabel.setText(_translate("addDialog", "学号"))
        self.namelabel.setText(_translate("addDialog", "姓名"))
        self.sexlabe.setText(_translate("addDialog", "性别"))
        self.agelabel.setText(_translate("addDialog", "年龄"))
        self.bornlabel.setText(_translate("addDialog", "出生日期"))
        self.phonelabel.setText(_translate("addDialog", "手机号码"))
        self.emaillabel.setText(_translate("addDialog", "电子邮箱"))
        self.homelabel.setText(_translate("addDialog", "家庭住址"))
        self.professlabel.setText(_translate("addDialog", "专业"))
        self.professcomboBox.setItemText(0, _translate("addDialog", "计算机科学与技术"))
        self.professcomboBox.setItemText(1, _translate("addDialog", "信息安全"))
        self.professcomboBox.setItemText(2, _translate("addDialog", "网络工程"))
        self.professcomboBox.setItemText(3, _translate("addDialog", "电子科学与技术"))