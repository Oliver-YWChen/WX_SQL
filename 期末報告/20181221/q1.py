import wx,sqlite3
class MySalgar(wx.Frame):
	def __init__(self):
		
		wx.Frame.__init__(self,parent=None,title=u"長度換算",size=(500,220))
		panel = wx.Panel(self)
		
		self.a = wx.TextCtrl(parent=panel,value="",pos=(10,10),size=(60,23))
		
		self.sampleList = ['mile', 'km', 'm', 'yard', 'ft', 'inch', 'cm' ,'mm']
		self.edithear=wx.ComboBox(panel, 30, "",
                                  wx.Point(80, 10), wx.Size(95, -1),
                                  self.sampleList, wx.CB_DROPDOWN)
		
		wx.StaticText(parent=panel,label=u"to",pos=(190,10),size=(23,50))
		
		self.sampleList2 = ['mile', 'km', 'm', 'yard', 'ft', 'inch', 'cm' ,'mm']
		self.edithear2=wx.ComboBox(panel, 31, "",
                                   wx.Point(215, 10), wx.Size(95, -1),
                                   self.sampleList2, wx.CB_DROPDOWN)
		
		
		
		
		self.btn = wx.Button(parent=panel,label=u"轉換",pos=(325,10))
		
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn)
		
		#新增 BtnClick 事件 -- 結束 --
		self.message = wx.StaticText(parent=panel,pos=(10,45))
		
		
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		a = float(self.a.GetValue())
		u1 = self.edithear.GetValue()
		u2 = self.edithear2.GetValue()
		
		conn = sqlite3.connect("Units.db")
		cursor = conn.cursor()
		sql = "SELECT * FROM length WHERE unit=?"
		cursor.execute(sql, [(u1)])
		T = cursor.fetchall()
		t = T[0]
		t1 = float(t[1])
		t2 = str(t[0])
		
		conn = sqlite3.connect("Units.db")
		cursor = conn.cursor()
		sql = "SELECT * FROM length WHERE unit=?"
		cursor.execute(sql, [(u2)])
		L = cursor.fetchall()
		l = L[0]
		l1 = float(l[1])
		l2 = str(l[0])
		
		out = a * t1 / l1
		
		w = str(a) + ' ' + t2 + ' ' + ' ' + '=' + ' ' + str(out) + ' ' + l2
		
		message1Str = str(w)
		self.message.SetLabel(message1Str)
		
	#撰寫 BtnClick 事件函式 -- 結束 --
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()