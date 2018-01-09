#!/usr/bin/python3
#coding=utf-8
import sys
import os
import phonebook
import xml.dom.minidom as DM
from PyQt5.QtWidgets import QApplication

def setXml():
	if os.path.exists(os.getcwd()+'/student.xml'):
		pass
	else:
		print(os.getcwd())
		DM.parse(os.getcwd()+'/stdent.xml')
		impl = DM.getDOMImplementation()
		dom = impl.createDocument(None,'students', None)
		f= open(os.getcwd()+'/student.xml', 'w', encoding='utf-8')
		dom.writexml(f, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
		f.close()

if __name__ == '__main__':
	setXml()
	app = QApplication(sys.argv)
	ui = phonebook.Ui_Students()
	ui.show()
	sys.exit(app.exec_())