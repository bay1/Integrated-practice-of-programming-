#!/usr/bin/python3
#coding=utf-8
import sys
import phonebook
from PyQt5.QtWidgets import QApplication

if 'studentMessages' not in vars():
    studentMessages = {}
    studentMessage = {}
else:
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = phonebook.Ui_Students()
    ui.show()
    sys.exit(app.exec_())