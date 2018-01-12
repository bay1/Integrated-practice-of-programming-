#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-12 00:01:09
# @Author  : Bayi
# @Link    : https://blog.flywinky.top/

import os
import wx
from game import startGame

class MyDialog(wx.Dialog): 
   def __init__(self, parent, title,picPath):
   	    image = wx.Image(picPath.encode('utf8'), wx.BITMAP_TYPE_ANY)
   	    temp = image.ConvertToBitmap()
   	    size = temp.GetWidth(), temp.GetHeight()
   	    super(MyDialog, self).__init__(parent, title = title, size = size)
   	    panel = wx.Panel(self)
   	    self.bmp = wx.StaticBitmap(self,-1,temp,size=size)

class Mywin(wx.Frame):
	def __init__(self, parent, title):
		super(Mywin, self).__init__(parent,title = title,size=((300,480)))
		self.InitUI()
	
	def InitUI(self):
		# 默认拼图格数
		self.VHNUMS = 3
		self.fileAddress=os.getcwd()+'/pic.jpg'
		self.SetMinSize((300,480))
		self.SetMaxSize((300,480))
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.icon = wx.Icon(os.getcwd()+"/favicon.ico", wx.BITMAP_TYPE_ICO)
		self.SetIcon(self.icon)

		self.startButton = wx.Button(self, label = u'开始游戏', pos = (100,20),size=(80,60))
		self.startButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.startButton.Bind(wx.EVT_BUTTON, lambda x:self.startButton_click())

		self.changePicButton = wx.Button(self, label = u'切换图片', pos = (100,90),size=(80,60))
		self.changePicButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.changePicButton.Bind(wx.EVT_BUTTON, lambda x:self.changePicButton_click())

		self.changeLevelButton = wx.Button(self, label = u'切换难度', pos = (100,160),size=(80,60))
		self.changeLevelButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.changeLevelButton.Bind(wx.EVT_BUTTON, lambda x:self.changeLevelButton_click())

		self.initPicButton = wx.Button(self, label = u'查看原图', pos = (100,230),size=(80,60))
		self.initPicButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.initPicButton.Bind(wx.EVT_BUTTON, lambda x:self.initPicButton_click())

		self.aboutButton = wx.Button(self, label = u'关于游戏', pos = (100,300),size=(80,60))
		self.aboutButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.aboutButton.Bind(wx.EVT_BUTTON, lambda x:self.aboutButton_click())

		self.quitButton = wx.Button(self, label = u'退出游戏', pos = (100,370),size=(80,60))
		self.quitButton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.quitButton.Bind(wx.EVT_BUTTON, lambda x:self.quitButton_click())

		self.Show(True)

		image = wx.Image((os.getcwd()+'/background.png').encode('utf8'), wx.BITMAP_TYPE_ANY)
		temp = image.ConvertToBitmap()
		size = temp.GetWidth(), temp.GetHeight()
		self.bmp = wx.StaticBitmap(self,-1,temp,pos=(10, 20),size=size)

	def startButton_click(self):
		startGame(self.fileAddress.encode('utf8'),self.VHNUMS)

	def changePicButton_click(self):
		dlg = wx.FileDialog(self, u"选择新图片",os.getcwd(),style=wx.DD_DEFAULT_STYLE,wildcard= "(*.jpg)|*.jpg|" "(*.png)|*.png")
		if dlg.ShowModal() == wx.ID_OK:
			self.fileAddress=dlg.GetPath()
		dlg.Destroy()

	def changeLevelButton_click(self):
		levelEntry = wx.TextEntryDialog(None, u"请输入要设置的分割数:", u"修改图片分割数",u'3')
		if levelEntry.ShowModal() == wx.ID_OK:
			message = levelEntry.GetValue()
			if str(message).isdigit() and int(message)>=3 and int(message)<=9:
				self.VHNUMS=int(message)
			else:
				wx.MessageBox("请检查输入!","提示")

		levelEntry.Destroy()

	def initPicButton_click(self):
		MyDialog(self, "原图",self.fileAddress).ShowModal()

	def aboutButton_click(self):
		wx.MessageBox("点击生成的白块,就可以开始拼图啦!","关于")

	def quitButton_click(self):
		self.Close(True)

if __name__ == '__main__':
	app = wx.App()
	Mywin(None,u'拼图游戏')
	app.MainLoop()