import re
import add
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from add import Ui_addDialog
from PyQt5.QtQuick import *

class Ui_Students(QDialog,QQuickView):
    def __init__(self):
        QWidget.__init__(self)
        self.initUi()

    def initUi(self):
        self.setMinimumSize(QtCore.QSize(1125, 594))
        self.setMaximumSize(QtCore.QSize(1125, 594))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(9)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.addButton = QtWidgets.QPushButton(self)
        self.addButton.setGeometry(QtCore.QRect(190, 20, 111, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/add_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addButton_click)
        self.editButton = QtWidgets.QPushButton(self)
        self.editButton.setGeometry(QtCore.QRect(320, 20, 111, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setObjectName("editButton")
        self.editButton.clicked.connect(self.editButton_click)
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setGeometry(QtCore.QRect(580, 20, 111, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon3)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchButton_click)
        self.deleteButton = QtWidgets.QPushButton(self)
        self.deleteButton.setGeometry(QtCore.QRect(450, 20, 111, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon4)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteButton_click)
        self.studentsTableWidget = QtWidgets.QTableWidget(self)
        self.studentsTableWidget.setEnabled(True)
        self.studentsTableWidget.setGeometry(QtCore.QRect(0, 90, 1125, 501))
        self.studentsTableWidget.setToolTipDuration(-1)
        self.studentsTableWidget.setStyleSheet("font: 9pt \"楷体\";")
        self.studentsTableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.studentsTableWidget.setLineWidth(1)
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
        self.studentsTableWidget.horizontalHeader().setDefaultSectionSize(124)
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
        self.backupButton = QtWidgets.QPushButton(self)
        self.backupButton.setGeometry(QtCore.QRect(710, 20, 111, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/backup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backupButton.setIcon(icon5)
        self.backupButton.setObjectName("backupButton")
        self.backupButton.clicked.connect(self.backupButton_click)
        self.redoButton = QtWidgets.QPushButton(self)
        self.redoButton.setGeometry(QtCore.QRect(840, 20, 111, 31))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon6)
        self.redoButton.setObjectName("redoButton")
        self.redoButton.clicked.connect(self.redoButton_click)
        self.studentsTableWidget.raise_()
        self.addButton.raise_()
        self.redoButton.raise_()
        self.deleteButton.raise_()
        self.searchButton.raise_()
        self.backupButton.raise_()
        self.editButton.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "通讯录"))
        self.addButton.setText(_translate("self", "添加"))
        self.editButton.setText(_translate("self", "编辑"))
        self.searchButton.setText(_translate("self", "查找"))
        self.deleteButton.setText(_translate("self", "删除"))
        item = self.studentsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("self", "学号"))
        item = self.studentsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("self", "姓名"))
        item = self.studentsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("self", "性别"))
        item = self.studentsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("self", "年龄"))
        item = self.studentsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("self", "出生日期"))
        item = self.studentsTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("students", "手机号码"))
        item = self.studentsTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("self", "家庭住址"))
        item = self.studentsTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("self", "电子邮箱"))
        item = self.studentsTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("self", "专业"))
        self.backupButton.setText(_translate("self", "备份"))
        self.redoButton.setText(_translate("self", "恢复"))

    def addButton_click(self):
        from add import Ui_addDialog
        addWindow= Ui_addDialog(self)
        addWindow.Signal_Add.connect(self.getDate)
        addWindow.show()

    def getDate(self,var:tuple):
        if var[1]==0:
            self.studentsTableWidget.insertRow(self.studentsTableWidget.rowCount())
        self.studentsTableWidget.setItem(var[0],var[1],QTableWidgetItem(var[2]))
        if self.studentsTableWidget.item(var[0],var[1]):
            self.studentsTableWidget.item(var[0],var[1]).setTextAlignment(QtCore.Qt.AlignCenter)

    def deleteButton_click(self):
        pass

    def editButton_click(self):
        pass

    def searchButton_click(self):
        pass

    def backupButton_click(self):
        pass

    def redoButton_click(self):
        pass