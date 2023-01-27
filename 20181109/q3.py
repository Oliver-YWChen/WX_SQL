import wx,string

class DirDialog(wx.Frame):
	""""""

	def __int__(self):
		"""Constructor"""
		wx.Frame.__int__(self, None, -1, u'資料夾選擇對話框')
		b = wx.Button(self, -1, u'資料夾選擇對話框')
		self.Bind(wx.EVT_BUTTON, self.OnButton, b)

	def OnButton(self, event):
		""""""
		dlg = wx.DirDialog(self, u'選擇資料夾', style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			print(dlg.GetPath())

		dlg.Destroy()

if __name__ == '__main__':
	frame = wx.PySimpleApp()
	app = DirDialog()
	app.Show()
	frame.MainLoop()

class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"薪資試算程式",size=(940,180))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"選擇要複製檔案",pos=(10,10))
		self.a = wx.TextCtrl(parent=panel,pos=(100,10),size=(700,23))
		wx.StaticText(parent=panel,label=u"選擇資料夾",pos=(10,50))
		self.b = wx.TextCtrl(parent=panel,pos=(100,50),size=(700,23))
		self.btn1 = wx.Button(parent=panel,label=u"瀏覽",pos=(810,10))
		self.btn2 = wx.Button(parent=panel,label=u"瀏覽",pos=(810,50))
		self.btn3 = wx.Button(parent=panel,label=u"複製",pos=(810,90))
		
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick1,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick2,self.btn2)
		self.Bind(wx.EVT_BUTTON,self.BtnClick3,self.btn3)
		
		#新增 BtnClick 事件 -- 結束 --

		
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick1(self,event):
		__int__(self)
		
	def BtnClick2(self,event):
		__int__(self)
		
	def BtnClick3(self,event):
		__int__(self)
		

	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()
	
