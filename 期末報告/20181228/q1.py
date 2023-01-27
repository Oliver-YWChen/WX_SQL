import wx,sqlite3
class MySalgar(wx.Frame):
	def __init__(self):
		
		wx.Frame.__init__(self,parent=None,title=u"村里查詢",size=(350,90))
		panel = wx.Panel(self)
		
		conn = sqlite3.connect("database.db")
		cursor = conn.cursor()
		sql = "SELECT DISTINCT cname FROM tables"
		cursor.execute(sql)
		L = cursor.fetchall()
		L1 = []
		n = 0
		for i in range(len(L)):
			t = L[n]
			L1.append(t[0])
			n = n + 1
		
		self.sampleList1 = L1
		self.edithear1=wx.ComboBox(panel, 30, "",
                                  wx.Point(10, 10), wx.Size(95, -1),
                                  self.sampleList1, wx.CB_DROPDOWN)
		
		self.sampleList2 = []
		self.edithear2=wx.ComboBox(panel, 31, "",
                                  wx.Point(120, 10), wx.Size(95, -1),
                                  self.sampleList2, wx.CB_DROPDOWN)
		
		self.sampleList3 = []
		self.edithear3=wx.ComboBox(panel, 32, "",
                                   wx.Point(230, 10), wx.Size(95, -1),
                                   self.sampleList3, wx.CB_DROPDOWN)
		
		for box in range(30,33,1):
			wx.EVT_COMBOBOX(self, box, self.EvtComboBox)
		
	def EvtComboBox(self, event):
		if event.GetId() == 30:
			conn = sqlite3.connect("database.db")
			cursor = conn.cursor()
			cursor.execute("SELECT DISTINCT tname FROM tables WHERE cname='%s'" %event.GetString())
			L = cursor.fetchall()
			n = 0
			self.edithear2.Clear()
			self.edithear3.Clear()
			for i in range(len(L)):
				t = L[n]
				self.edithear2.Append(t[0])
				n = n + 1
				
		elif event.GetId() == 31:
			conn = sqlite3.connect("database.db")
			cursor = conn.cursor()
			cursor.execute("SELECT DISTINCT vname FROM tables WHERE tname='%s'" %event.GetString())
			L = cursor.fetchall()
			n = 0
			self.edithear3.Clear()
			for i in range(len(L)):
				t = L[n]
				self.edithear3.Append(t[0])
				n = n + 1
				
				
if __name__ 	== '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()