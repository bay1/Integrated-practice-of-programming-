import tkinter
import os
import re
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkfont

class Calculator(object):
	"""计算器"""
	def __init__(self):
		self.tk=tkinter.Tk() #实例化
		self.tk.title('计算器')
		self.tk.minsize(370,460)
		self.tk.maxsize(400,400)
		self.tk.iconbitmap(os.getcwd()+'/favicon.ico')
		self.inputlist=[]
		self.midstr=''
		self.ButtonList=['清空','/','*','退格',7,8,9,'-',4,5,6,'+',1,2,3,0,'.','=','1/x','%','sqrt']
		#增加菜单
		self.menuBar=Menu(self.tk)
		self.tk.config(menu=self.menuBar)
		#设置菜单选项
		aboutMenu=Menu(self.menuBar,tearoff=0)
		moreMenu=Menu(self.menuBar,tearoff=0)
		self.menuBar.add_cascade(label='拓展',menu=moreMenu)
		self.menuBar.add_cascade(label='帮助',menu=aboutMenu)
		aboutMenu.add_command(label='关于',command=self.about)
		moreMenu.add_command(label='基本养老保险金',command=startBaoxian)
		#字体设置
		self.EntryFont=tkfont.Font(self.tk,size=13)
		self.ButtonFont=tkfont.Font(self.tk,size=12)
		#面板显示
		self.count=tkinter.StringVar()
		self.count.set('0')
		self.label=tkinter.Label(self.tk,bg='#EEE9E9',bd='3',fg='black',anchor='center',font=self.EntryFont,textvariable=self.count)
		self.label.place(y=10,width=380,height=40)
		#按钮设置
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#EE6A50',text=self.ButtonList[0],
			font=self.ButtonFont,command=self.clear)
		self.NumButton.place(x=30,y=80,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[1],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[1]))
		self.NumButton.place(x=110,y=80,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[2],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[2]))
		self.NumButton.place(x=190,y=80,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#EE6A50',text=self.ButtonList[3],
			font=self.ButtonFont,command=self.backspace)
		self.NumButton.place(x=270,y=80,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[4],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[4]))
		self.NumButton.place(x=30,y=140,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[5],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[5]))
		self.NumButton.place(x=110,y=140,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[6],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[6]))
		self.NumButton.place(x=190,y=140,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[7],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[7]))
		self.NumButton.place(x=270,y=140,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[8],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[8]))
		self.NumButton.place(x=30,y=200,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[9],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[9]))
		self.NumButton.place(x=110,y=200,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[10],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[10]))
		self.NumButton.place(x=190,y=200,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[11],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[11]))
		self.NumButton.place(x=270,y=200,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[12],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[12]))
		self.NumButton.place(x=30,y=260,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[13],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[13]))
		self.NumButton.place(x=110,y=260,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[14],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[14]))
		self.NumButton.place(x=190,y=260,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#CDBA96',text=self.ButtonList[15],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[15]))
		self.NumButton.place(x=30,y=320,width=150,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#EECFA1',text=self.ButtonList[16],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[16]))
		self.NumButton.place(x=190,y=320,width = 70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#E0EEE0',text=self.ButtonList[17],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[17]))
		self.NumButton.place(x=270,y=260,width=70,height=175)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[18],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[18]))
		self.NumButton.place(x=30,y=380,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[19],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[19]))
		self.NumButton.place(x=110,y=380,width=70,height=55)
		self.NumButton=tkinter.Button(master=self.tk,relief=GROOVE,bg='#BFEFFF',text=self.ButtonList[20],
			font=self.ButtonFont,command=lambda:self.knobDown(self.ButtonList[20]))
		self.NumButton.place(x=190,y=380,width=70,height=55)
	
	#关于
	def about(self):
		messagebox.showinfo('关于', ' 作者：八一 \n verion 1.0 \n 感谢您的使用！')

	#清空
	def clear(self):
		self.inputlist=[]
		self.midstr=''
		self.count.set(0)

	#退格
	def backspace(self):
		if self.inputlist==[]:
			pass
		else:
			self.inputlist.pop()
			self.count.set(self.inputlist)

	#判断计算符号
	def signCheck(self,sign):
		return sign in self.inputlist

	def checkList(self):
		result=0
		locate=-1
		listSum=0
		for length in range(0,len(self.inputlist)):
			if re.findall(r'[-+*/]',str(self.inputlist[length])):
				result=1
				if length>locate:
					locate=length
			else:
				pass
		if result==1:
			for i in range(locate+1,len(self.inputlist)):
				listSum+=int(self.inputlist[i])*(10**(len(self.inputlist)-i-1))
		else:
			for j in range(0,len(self.inputlist)):
				listSum+=int(self.inputlist[j])*(10**(len(self.inputlist)-j-1))
		return listSum,locate	

	#添加button
	def addButton(self,button):
		if button==self.ButtonList[18]:
			listSum,locate=self.checkList()
			if locate==-1:
				self.inputlist=[str(round(eval('1/'+str(listSum)),5))]
			else:
				for k in range(locate+1,len(self.inputlist)):
					del self.inputlist[k]
				self.inputlist.append(str(round(eval('1/'+str(listSum)),5)))
		elif button==self.ButtonList[19]:
			listSum,locate=self.checkList()
			if locate==-1:
				self.inputlist=[str(listSum*0.01)]
			else:
				for k in range(locate+1,len(self.inputlist)):
					del self.inputlist[k]
				self.inputlist.append(str(listSum*0.01))
		elif button==self.ButtonList[20]:
			listSum,locate=self.checkList()
			if locate==-1:
				self.inputlist=[str(round(listSum**0.5,5))]
			else:
				for k in range(locate+1,len(self.inputlist)):
					del self.inputlist[k]
				self.inputlist.append(str(round(listSum**0.5,5)))
		else:
			self.inputlist.append(button)
		self.count.set(self.inputlist)

	#检查输入
	def inputCheck(self,input):
		if re.findall(r'[&a-zA-Z<>,?~!@#$";:]',str(input)):
			if input=='1/x' or input=='%' or input=='sqrt':
				pass
			else:
				self.count.set('非法')	

	#按钮事件处理
	def knobDown(self,button):
		self.inputCheck(button)
		#inputlist为空时，检查输入的第一位是否为数字
		if self.inputlist==[] and re.findall(r'[-+*/=.%]',str(button)):
			self.count.set('符号不能放在第一位哦~')
		#如果输入算符
		elif re.findall(r'[-+*/]',str(button)):
			#判断inputlist里面是否有算符
			if self.signCheck('-') or self.signCheck('+') \
				or self.signCheck('/') or self.signCheck('*'):
				if re.findall(r'[-+*/]',str(self.inputlist[-1])):
					if button=='1/x' or button=='%':
						pass
					else:
						self.count.set('不能连续输入算符')
				else:
					self.addButton(button)
			else:
				self.addButton(button)
		#输入等号时转化为str利用eval函数计算		
		elif button=='=':
			if re.findall(r'[-+*/%]',str(self.inputlist[-1])):
				self.count.set('结尾不能是算符哦~')
			else:
				for length in range(0,len(self.inputlist)):
					if str(self.inputlist[length]).isdigit():
						self.midstr+=str(self.inputlist[length])
					else:
						self.midstr=self.midstr+self.inputlist[length]
				self.inputCheck(self.midstr) #eval函数很危险要严格过滤
				self.count.set(self.midstr+'='+str(round(eval(self.midstr),5)))
				self.inputlist=[]
				self.midstr=''
		else:
			self.addButton(button)

	def start(self):
		self.tk.mainloop()

class Baoxian(object):
	"""docstring for Baoxian"""
	def __init__(self):
		super(Baoxian, self).__init__()
		self.baoxianTk=tkinter.Tk()
		self.baoxianTk.title('基本养老保险金计算器')
		self.baoxianTk.maxsize(400,500)
		self.baoxianTk.minsize(400,500)
		self.baoxianTk.iconbitmap(os.getcwd()+'/favicon.ico')
		#字体设置
		self.EntryFont=tkfont.Font(self.baoxianTk,size=13)
		self.ButtonFont=tkfont.Font(self.baoxianTk,size=12)
		self.checkNum=self.baoxianTk.register(self.validateNum)
		Label(self.baoxianTk,text='您上年度平均月',font=("Arial,6")).place(x=30,y=10)
		Label(self.baoxianTk,text='工资(元)',font=("Arial,6")).place(x=30,y=35)
		Label(self.baoxianTk,text='本市职工上年度',font=("Arial,6")).place(x=30,y=70)
		Label(self.baoxianTk,text='平均月工资(元)',font=("Arial,6")).place(x=30,y=95)
		Label(self.baoxianTk,text='单位缴存比例(%)',font=("Arial,6")).place(x=30,y=140)
		Label(self.baoxianTk,text='个人缴存比例(%)',font=("Arial,6")).place(x=30,y=190)
		Label(self.baoxianTk,text='每月缴存基本',font=("Arial,6")).place(x=30,y=300)
		Label(self.baoxianTk,text='养老保险金(元)',font=("Arial,6")).place(x=30,y=325)
		Label(self.baoxianTk,text='单位缴存(元)',font=("Arial,6")).place(x=30,y=370)
		Label(self.baoxianTk,text='个人缴存(元)',font=("Arial,6")).place(x=30,y=420)
		self.yuecunCount=Label(self.baoxianTk,bg='white',bd='3',fg='#8B795E',font=self.EntryFont)
		self.yuecunCount.place(x=190,y=310,width=200)
		self.danweiCount=Label(self.baoxianTk,bg='white',bd='3',fg='#8B795E',font=self.EntryFont)
		self.danweiCount.place(x=190,y=370,width=200)
		self.gerenCount=Label(self.baoxianTk,bg='white',bd='3',fg='#8B795E',font=self.EntryFont)
		self.gerenCount.place(x=190,y=420,width=200)
		self.selfEntry=Entry(self.baoxianTk,validate='key',validatecommand=(self.checkNum,'%P'),font=self.EntryFont)
		self.selfEntry.place(x=190,y=20)
		self.shiEntry=Entry(self.baoxianTk,validate='key',validatecommand=(self.checkNum,'%P'),font=self.EntryFont)
		self.shiEntry.place(x=190,y=80)
		self.danweiEntry=Entry(self.baoxianTk,validate='key',validatecommand=(self.checkNum,'%P'),font=self.EntryFont)
		self.danweiEntry.place(x=190,y=140)
		self.gerenEntry=Entry(self.baoxianTk,validate='key',validatecommand=(self.checkNum,'%P'),font=self.EntryFont)
		self.gerenEntry.place(x=190,y=190)
		self.shiEntry.insert(10,2360)
		self.danweiEntry.insert(10,20)
		self.gerenEntry.insert(10,8)
		Button(self.baoxianTk,text='计算',bg='#E0EEE0',font=self.ButtonFont,command=self.count).place(x=80,y=240,width=100,height=40)
		Button(self.baoxianTk,text='重新计算',bg='#E0EEE0',font=self.ButtonFont,command=lambda:self.recount()).place(x=220,y=240,width=100,height=40)

	#验证是否输入数字	
	def validateNum(self,content):
		if content.isdigit() and int(content)>=0 or content=="":
			return True
		else:
			return False

	#计算
	def count(self):
		if int(self.selfEntry.get())>int(self.shiEntry.get())*0.6 and int(self.selfEntry.get())<int(self.shiEntry.get())*3:
			self.danweiCount['text']=int(self.selfEntry.get())*int(self.danweiEntry.get())/100
			self.gerenCount['text']=int(self.selfEntry.get())*int(self.gerenEntry.get())/100
			self.yuecunCount['text']=int(self.selfEntry.get())*int(self.danweiEntry.get())/100+int(self.selfEntry.get())*int(self.gerenEntry.get())/100
		elif int(self.selfEntry.get())>=int(self.shiEntry.get())*3:
			self.danweiCount['text']=int(self.shiEntry.get())*3*int(self.danweiEntry.get())/100
			self.gerenCount['text']=int(self.shiEntry.get())*3*int(self.gerenEntry.get())/100
			self.yuecunCount['text']=int(self.shiEntry.get())*3*int(self.gerenEntry.get())/100+int(self.shiEntry.get())*3*int(self.danweiEntry.get())/100
		elif int(self.selfEntry.get())<=int(self.shiEntry.get())*0.6:
			self.danweiCount['text']=int(self.shiEntry.get())*0.6*int(self.danweiEntry.get())/100
			self.gerenCount['text']=int(self.shiEntry.get())*0.6*int(self.gerenEntry.get())/100
			self.yuecunCount['text']=int(self.shiEntry.get())*0.6*int(self.gerenEntry.get())/100+int(self.shiEntry.get())*3*int(self.danweiEntry.get())/100
		else:
			pass

	#重新计算
	def recount(self):
		self.selfEntry.delete(0,END)
		self.shiEntry.delete(0,END)
		self.danweiEntry.delete(0,END)
		self.gerenEntry.delete(0,END)

	def start(self):
		self.baoxianTk.mainloop()		

def startBaoxian():
	NewBaoxian=Baoxian()
	NewBaoxian.start()

if __name__ == '__main__':
	NewCalculator=Calculator()
	NewCalculator.start()