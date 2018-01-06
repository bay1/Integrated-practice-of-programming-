#!/usr/bin/python3
#coding=utf-8
import sys
import phonebook
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = phonebook.Ui_students()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())