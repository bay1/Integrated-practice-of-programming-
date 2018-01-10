#!/usr/bin/python3
#coding=utf-8
import sys
import os
import phonebook
from lxml import etree
from PyQt5.QtWidgets import QApplication

def setXml():
	if os.path.exists(os.getcwd()+'/student.xml'):
		pass
	else:
		root = etree.Element('students')
		tree = etree.ElementTree(root)
		tree.write(os.getcwd()+'/student.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

if __name__ == '__main__':
	setXml()
	app = QApplication(sys.argv)
	ui = phonebook.Ui_Students()
	ui.show()
	sys.exit(app.exec_())