#coding=utf-8
import re
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import *
from run import studentMessages,studentMessage

def addButton_click():
    from add import Ui_addDialog
    addWindow= Ui_addDialog()
    addWindow.show()

def addStudent(id, name, man, women, age, borndate, phone, email, home, profession, diaglog):
    updateTable(studentMessages)
    if id.isdigit() and phone.isdigit() and validateChinese(name) != 0 and validateChinese(home) != 0:
        checkIdResult = validateId(id)
        if checkIdResult == 1:
            if validateEmail(email) == 1:
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
                updateTable(studentMessages)
                QMessageBox.information(diaglog, "提示", diaglog.tr("添加成功!"))
                diaglog.close()
            else:
                QMessageBox.information(diaglog, "提示", diaglog.tr("邮箱错误!"))
        else:
            QMessageBox.information(diaglog, "提示", diaglog.tr("学号已存在!"))
    else:
        QMessageBox.information(diaglog, "提示", diaglog.tr("请检查输入!"))

def validateChinese(str):
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    result = re.findall(pattern, str)
    if str is None or len(result) == 0:
        return 0
    else:
        if result[0] != str:
            return 0
        else:
            return 1

def validateEmail(email):
    str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
    if len(email) > 7:
        if re.match(str, email):
            return 1
    return 0

def validateId(addId):
    checkSign = 1
    for student in studentMessages.keys():
        if addId == student:
            checkSign = 0
    return checkSign

def updateTable(dict):
    from phonebook import Ui_Students
    ui = Ui_Students()
    ui.studentsTableWidget.setItem(1,1,QTableWidgetItem("45614556"))
    line = -1
    headerList = ['ID', 'name', 'sex', 'age', 'borndate', 'phone', 'home', 'email', 'profession']
    sorted(studentMessages.items(), key=lambda e: e[0], reverse=True)
    for student in studentMessages:
        line += 1
        for column in range(0, 9):
            content="%s"%studentMessages[student][headerList[column]]
            ui.studentsTableWidget.setItem(line,column,QTableWidgetItem(content))
            ui.studentsTableWidget.item(line, column).setTextAlignment(QtCore.Qt.AlignCenter)

def deleteButton_click():
    pass

def editButton_click():
    pass

def searchButton_click():
    pass

def backupButton_click():
    pass

def redoButton_click():
    pass