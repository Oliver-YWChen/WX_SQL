import wx,sqlite3
class MySalgar(wx.Frame):
	def __init__(self):
		
		wx.Frame.__init__(self,parent=None,title=u"單位換算",size=(500,220))
		panel = wx.Panel(self)
		
		self.sampleList3 = ['長度', '面積']
		self.edithear3=wx.ComboBox(panel, 30, "",
                                  wx.Point(10, 10), wx.Size(95, -1),
                                  self.sampleList3, wx.CB_DROPDOWN)
		
		self.a = wx.TextCtrl(parent=panel,value="",pos=(10,45),size=(60,23))
		
		self.sampleList = []
		self.sampleList2 = []
		
		self.edithear=wx.ComboBox(panel, 30, "",
                                  wx.Point(80, 45), wx.Size(95, -1),
                                  self.sampleList, wx.CB_DROPDOWN)
		
		wx.StaticText(parent=panel,label=u"to",pos=(190,45),size=(23,50))
		
		self.edithear2=wx.ComboBox(panel, 31, "",
                                   wx.Point(215, 45), wx.Size(95, -1),
                                   self.sampleList2, wx.CB_DROPDOWN)
		
		self.btn = wx.Button(parent=panel,label=u"轉換",pos=(325,45))
		
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn)
		
		#新增 BtnClick 事件 -- 結束 --
		self.message = wx.StaticText(parent=panel,pos=(10,80))
		
		for box in range(30,32,1):
			wx.EVT_COMBOBOX(self, box, self.EvtComboBox)
		
	def EvtComboBox(self, event):
		if event.GetId() == 30:
			if event.GetString() == '長度':
				self.edithear.Clear()
				self.edithear2.Clear()
				self.sampleList = ['mile', 'km', 'm', 'yard', 'ft', 'inch', 'cm' ,'mm']
				self.sampleList2 = ['mile', 'km', 'm', 'yard', 'ft', 'inch', 'cm' ,'mm']
				self.edithear.Append(self.sampleList)
				self.edithear2.Append(self.sampleList2)
				
			if event.GetString() == '面積':
				self.edithear.Clear()
				self.edithear2.Clear()
				self.sampleList = ['平方公尺', '平方公里', '公頃', '英畝', '公畝', '甲', '分' ,'坪']
				self.sampleList2 = ['平方公尺', '平方公里', '公頃', '英畝', '公畝', '甲', '分' ,'坪']
				self.edithear.Append(self.sampleList)
				self.edithear2.Append(self.sampleList2)
				
			
			
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		
		if self.edithear3.GetValue() == '長度':
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
		
		if self.edithear3.GetValue() == '面積':
			a = float(self.a.GetValue())
			u1 = self.edithear.GetValue()
			u2 = self.edithear2.GetValue()
			
			conn = sqlite3.connect("Units.db")
			cursor = conn.cursor()
			sql = "SELECT * FROM area WHERE unit=?"
			cursor.execute(sql, [(u1)])
			T = cursor.fetchall()
			t = T[0]
			t1 = float(t[1])
			t2 = str(t[0])
			
			conn = sqlite3.connect("Units.db")
			cursor = conn.cursor()
			sql = "SELECT * FROM area WHERE unit=?"
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