import wx,string,random
class MySalgar(wx.Frame):
	global anw,b,c,n
	def __init__(self):
		global n
		n = 0
		wx.Frame.__init__(self,parent=None,title=u"終極密碼",size=(350,320))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"請輸入密碼範圍",pos=(10,30))
		self.b = wx.TextCtrl(parent=panel,pos=(100,30),size=(60, 23))
		wx.StaticText(parent=panel,label=u"~",pos=(170,30))
		self.c = wx.TextCtrl(parent=panel,pos=(190,30),size=(60, 23))
		self.btn3 = wx.Button(parent=panel,label=u"送出",pos=(10,80))
                              
		wx.StaticText(parent=panel,label=u"請輸入密碼",pos=(10,130))
		self.a = wx.TextCtrl(parent=panel,pos=(100,130),size=(60, 23))      
		self.btn1 = wx.Button(parent=panel,label=u"確認",pos=(10,210))
		self.btn2 = wx.Button(parent=panel,label=u"重來",pos=(120,210))

		self.Bind(wx.EVT_BUTTON,self.BtnClick1,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick2,self.btn2)
		self.Bind(wx.EVT_BUTTON,self.BtnClick3,self.btn3)

		self.message1 = wx.StaticText(parent=panel,pos=(10,170),size=(30,30))
		self.message2 = wx.StaticText(parent=panel,pos=(180,130),size=(30,30))
    
	def BtnClick3(self,event):
		global anw,b,c,n
		b = int(self.b.GetValue())
		c = int(self.c.GetValue())
		n = 0
		anw = int(random.randint(b,c))
        
	def BtnClick1(self,event):
		global anw,b,c,n
		a = self.a.GetValue()
		a = int(a)
		n = n + 1
		messageStr2 = '你已猜了%d次' %n
		if a > c:
			messageStr = '太大　超出範圍啦！'         
		elif a < b:
			messageStr = '太小　超出範圍啦！'
		elif a > anw:
			messageStr = '數字太大'
		elif a < anw:
			messageStr = '數字太小'
		elif a == anw:
			messageStr = '猜中啦！'
			n = n - 1            
		self.message1.SetLabel(messageStr)
		self.message2.SetLabel(messageStr2)
 
	def BtnClick2(self,event):
		global anw,b,c,n
		self.message1.SetLabel('')
		self.message2.SetLabel('')
		anw = int(random.randint(b,c))            
		n = 0
        
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()