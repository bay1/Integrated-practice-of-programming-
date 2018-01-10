# -*- coding: utf-8 -*-
import re
import os
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from lxml import etree

studentMessage={}

class Ui_addDialog(QDialog):
    Signal_Add = pyqtSignal(tuple)
    def __init__(self,parent=None):
        super(Ui_addDialog,self).__init__(parent)
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
        self.confirmButton.clicked.connect(self.addStudent)

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

    def emitSign(self,var:tuple):
        self.Signal_Add.emit(var)

    def addStudent(self):
        id=self.idlineEdit.text()
        name=self.namelineEdit.text()
        man=self.radioButton_man
        women=self.radioButton_women
        age=self.agespinBox.value()
        borndate=self.borndateEdit.text()
        phone=self.phonelineEdit.text()
        email=self.emaillineEdit.text()
        home=self.homelineEdit.text()
        profession=self.professcomboBox.currentText()
        if id.isdigit() and phone.isdigit() and self.validateChinese(name) != 0 and self.validateChinese(home) != 0:
            checkIdResult = self.validateId(id)
            if checkIdResult == 1:
                if self.validateEmail(email) == 1:
                    if man.isChecked():
                        sex = '男'
                    elif women.isChecked():
                        sex = '女'
                    else:
                        sex = '妖'
                    studentMessage['ID'] = id
                    studentMessage['name'] = name
                    studentMessage['sex'] = sex
                    studentMessage['age'] = str(age)
                    studentMessage['borndate'] = borndate
                    studentMessage['phone'] = phone
                    studentMessage['email'] = email
                    studentMessage['home'] = home
                    studentMessage['profession'] = profession
                    xml=etree.parse(os.getcwd()+'/student.xml')
                    root = xml.getroot()
                    student=etree.Element("student"+id)
                    root.append(student)
                    for key,val in sorted(studentMessage.items(), key=lambda e:e[0], reverse=True):
                        key = etree.SubElement(student, key)
                        key.text = val
                    xml.write(os.getcwd()+'/student.xml', pretty_print=True, encoding='utf-8')
                    self.updateTable()
                    QMessageBox.information(self, "提示", self.tr("添加成功!"))
                    self.close()
                else:
                    QMessageBox.information(self, "提示", self.tr("邮箱错误!"))
            else:
                QMessageBox.information(self, "提示", self.tr("学号已存在!"))
        else:
            QMessageBox.information(self, "提示", self.tr("请检查输入!"))

    def validateChinese(self,str):
        pattern = re.compile(u"[\u4e00-\u9fa5]+")
        result = re.findall(pattern, str)
        if str is None or len(result) == 0:
            return 0
        else:
            if result[0] != str:
                return 0
            else:
                return 1

    def validateEmail(self,email):
        str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if len(email) > 7:
            if re.match(str, email):
                return 1
        return 0

    def validateId(self,addId):
        checkSign = 1
        studentMessages=self.xml_to_dict()
        for student in studentMessages.keys():
            if addId == student:
                checkSign = 0
        return checkSign

    def updateTable(self):
        line = -1
        studentMessages=self.xml_to_dict()
        headerList = ['ID', 'name', 'sex', 'age', 'borndate', 'phone', 'home', 'email', 'profession']
        sorted(studentMessages.items(), key=lambda e: e[0], reverse=True)
        for student in studentMessages:
            line += 1
            for column in range(0, 9):
                self.emitSign((line,column,studentMessages[student][headerList[column]]))

    def xml_to_dict(self):
        dict_new = {}
        doc=etree.parse(os.getcwd()+'/student.xml')
        root_name = doc.getroot()
        for key,value in enumerate(root_name):
            dict_init = {}
            list_init = []
            for item in value:
                if item.tag=='ID':
                    ID=item.text
                list_init.append([item.tag, item.text])
                for lists in list_init:
                    dict_init[lists[0]] = lists[1]
            dict_new[ID] = dict_init
        return dict_new