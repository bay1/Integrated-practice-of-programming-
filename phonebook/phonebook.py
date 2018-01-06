# -*- coding: utf-8 -*-

import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from add import Ui_addDialog
from PyQt5.QtQuick import *

if 'studentMessages' not in vars():
    studentMessages = {}
    studentMessage = {}
else:
    pass

class fun():
    def  __init__(self):
        super(fun, self).__init__()

    def addStudent(self,id, name, man, women, age, borndate, phone, email, home, profession, diaglog):
        ui=Ui_students()
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
                    studentMessage['age'] = age
                    studentMessage['borndate'] = borndate
                    studentMessage['phone'] = phone
                    studentMessage['email'] = email
                    studentMessage['home'] = home
                    studentMessage['profession'] = profession
                    studentMessages[id] = studentMessage
                    ui.updateTable(studentMessages)
                    QMessageBox.information(diaglog, "提示", diaglog.tr("添加成功!"))
                    diaglog.close()
                else:
                    QMessageBox.information(diaglog, "提示", diaglog.tr("邮箱错误!"))
            else:
                QMessageBox.information(diaglog, "提示", diaglog.tr("学号已存在!"))
        else:
            QMessageBox.information(diaglog, "提示", diaglog.tr("请检查输入!"))

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
        for student in studentMessages.keys():
            if addId == student:
                checkSign = 0
        return checkSign

class Ui_students(QQuickView,object):

    def __init__(self):
        super(Ui_students, self).__init__()

    def setupUi(self, students):
        students.setObjectName("students")
        students.resize(1125, 594)
        students.setMinimumSize(QtCore.QSize(1125, 594))
        students.setMaximumSize(QtCore.QSize(1125, 594))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(9)
        students.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        students.setWindowIcon(icon)
        self.addButton = QtWidgets.QPushButton(students)
        self.addButton.setGeometry(QtCore.QRect(190, 20, 111, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/add_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addButton_click)
        self.editButton = QtWidgets.QPushButton(students)
        self.editButton.setGeometry(QtCore.QRect(320, 20, 111, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setObjectName("editButton")
        self.editButton.clicked.connect(self.editButton_click)
        self.searchButton = QtWidgets.QPushButton(students)
        self.searchButton.setGeometry(QtCore.QRect(580, 20, 111, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon3)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchButton_click)
        self.deleteButton = QtWidgets.QPushButton(students)
        self.deleteButton.setGeometry(QtCore.QRect(450, 20, 111, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon4)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteButton_click)
        self.studentsTableWidget = QtWidgets.QTableWidget(students)
        self.studentsTableWidget.setEnabled(True)
        self.studentsTableWidget.setGeometry(QtCore.QRect(160, 90, 961, 501))
        self.studentsTableWidget.setToolTipDuration(-1)
        self.studentsTableWidget.setStyleSheet("font: 9pt \"楷体\";")
        self.studentsTableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.studentsTableWidget.setLineWidth(1)
        self.studentsTableWidget.setRowCount(20)
        self.studentsTableWidget.setColumnCount(9)
        self.studentsTableWidget.setObjectName("studentsTableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setUnderline(False)
        item.setFont(font)
        self.studentsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTableWidget.setHorizontalHeaderItem(8, item)
        self.studentsTableWidget.horizontalHeader().setVisible(True)
        self.studentsTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.studentsTableWidget.horizontalHeader().setDefaultSectionSize(106)
        self.studentsTableWidget.horizontalHeader().setHighlightSections(False)
        self.studentsTableWidget.horizontalHeader().setMinimumSectionSize(54)
        self.studentsTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.studentsTableWidget.horizontalHeader().setStretchLastSection(False)
        self.studentsTableWidget.verticalHeader().setVisible(False)
        self.studentsTableWidget.verticalHeader().setHighlightSections(True)
        self.studentsTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.studentsTableWidget.verticalHeader().setStretchLastSection(False)
        self.studentsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) #表格内容禁止编辑
        self.studentsTableWidget.setSortingEnabled(True) #设置单击表头进行数据排序
        self.studentsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows) #整行选中的方式
        self.studentsTableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection) #设置可以选中多个目标
        self.treeWidget = QtWidgets.QTreeWidget(students)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(0, 90, 161, 501))
        font = QtGui.QFont()
        font.setFamily("楷体")
        self.treeWidget.setFont(font)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.backupButton = QtWidgets.QPushButton(students)
        self.backupButton.setGeometry(QtCore.QRect(710, 20, 111, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/backup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backupButton.setIcon(icon5)
        self.backupButton.setObjectName("backupButton")
        self.backupButton.clicked.connect(self.backupButton_click)
        self.redoButton = QtWidgets.QPushButton(students)
        self.redoButton.setGeometry(QtCore.QRect(840, 20, 111, 31))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon6)
        self.redoButton.setObjectName("redoButton")
        self.redoButton.clicked.connect(self.redoButton_click)
        self.studentsTableWidget.raise_()
        self.treeWidget.raise_()
        self.addButton.raise_()
        self.redoButton.raise_()
        self.deleteButton.raise_()
        self.searchButton.raise_()
        self.backupButton.raise_()
        self.editButton.raise_()

        self.retranslateUi(students)
        QtCore.QMetaObject.connectSlotsByName(students)

        self.addWindow=QMainWindow()
        addUIWindows = Ui_addDialog()
        addUIWindows.setupUi(self.addWindow)

    def retranslateUi(self, students):
        _translate = QtCore.QCoreApplication.translate
        students.setWindowTitle(_translate("students", "通讯录"))
        self.addButton.setText(_translate("students", "添加"))
        self.editButton.setText(_translate("students", "编辑"))
        self.searchButton.setText(_translate("students", "查找"))
        self.deleteButton.setText(_translate("students", "删除"))
        item = self.studentsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("students", "学号"))
        item = self.studentsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("students", "姓名"))
        item = self.studentsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("students", "性别"))
        item = self.studentsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("students", "年龄"))
        item = self.studentsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("students", "出生日期"))
        item = self.studentsTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("students", "手机号码"))
        item = self.studentsTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("students", "家庭住址"))
        item = self.studentsTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("students", "电子邮箱"))
        item = self.studentsTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("students", "专业"))
        self.treeWidget.headerItem().setText(0, _translate("students", "全部"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("students", "计算机科学与技术"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("students", "信息安全"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("students", "网络工程"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("students", "电子科学与技术"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.backupButton.setText(_translate("students", "备份"))
        self.redoButton.setText(_translate("students", "恢复"))

    def addButton_click(self):
        self.addWindow.show()

    def deleteButton_click(self):
        self.addWindow.show()

    def editButton_click(self):
        self.addWindow.show()

    def searchButton_click(self):
        self.addWindow.show()

    def backupButton_click(self):
        self.addWindow.show()

    def redoButton_click(self):
        self.updateTable(233)
        #self.addWindow.show()

    def updateTable(self,dict):
        print(dict)
        line = 0
        headerList = ['ID', 'name', 'sex', 'age', 'borndate', 'phone', 'email', 'home', 'profession']
        sorted(studentMessages.items(), key=lambda e: e[0], reverse=True)
        assert isinstance(self.studentsTableWidget, object)
        self.studentsTableWidget.setItem(1, 1, QTableWidgetItem(studentMessages[1][headerList[0]]))
        for student in studentMessages:
            line += 1
            for column in range(0, 9):
                self.studentsTableWidget.setItem(line,column,QTableWidgetItem(studentMessages[student][headerList[column]]))