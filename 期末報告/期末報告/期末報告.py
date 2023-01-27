import wx,sqlite3
import openpyxl
from openpyxl import Workbook
class MySalgar(wx.Frame):
	def __init__(self):
		
		wx.Frame.__init__(self,parent=None,title=u"郵遞區號查詢",size=(590,130))
		panel = wx.Panel(self)
		
		conn = sqlite3.connect("郵遞區號.db")
		cursor = conn.cursor()
		sql = "SELECT DISTINCT City FROM tables"
		cursor.execute(sql)
		L = cursor.fetchall()
		
		L1 = []
		n = 0
		for i in range(len(L)):
			t = L[n]
			L1.append(t[0])
			n = n + 1
		
		self.sampleList1 = L1
		self.edithear1=wx.ComboBox(panel, 30, "選擇縣市",
                                  wx.Point(10, 10), wx.Size(95, -1),
                                  self.sampleList1, wx.CB_DROPDOWN)
		
		self.sampleList2 = []
		self.edithear2=wx.ComboBox(panel, 31, "選擇區",
                                  wx.Point(120, 10), wx.Size(95, -1),
                                  self.sampleList2, wx.CB_DROPDOWN)
		
		self.sampleList3 = []
		self.edithear3=wx.ComboBox(panel, 32, "選擇路段",
                                   wx.Point(230, 10), wx.Size(95, -1),
                                   self.sampleList3, wx.CB_DROPDOWN)
		
		self.sampleList4 = []
		self.edithear4=wx.ComboBox(panel, 33, "選擇門牌號",
                                   wx.Point(340, 10), wx.Size(115, -1),
                                   self.sampleList4, wx.CB_DROPDOWN)
		
		self.btn1 = wx.Button(parent=panel,label=u"查詢",pos=(470,10))
		
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn1)
		
		self.message = wx.StaticText(parent=panel,pos=(15,55))
		
		for box in range(30,34,1):
			wx.EVT_COMBOBOX(self, box, self.EvtComboBox)
		
	def EvtComboBox(self, event):
		if event.GetId() == 30:
			conn = sqlite3.connect("郵遞區號.db")
			cursor = conn.cursor()
			cursor.execute("SELECT DISTINCT Area FROM tables WHERE City='%s'" %event.GetString())
			L = cursor.fetchall()
			
			self.edithear2.Clear()
			self.edithear3.Clear()
			self.edithear4.Clear()
			self.edithear2.SetValue('選擇區')
			self.edithear3.SetValue('選擇路段')
			self.edithear4.SetValue('選擇門牌號')
			message1Str = ''
			self.message.SetLabel(message1Str)
			
			n = 0
			for i in range(len(L)):
				t = L[n]
				self.edithear2.Append(t[0])
				n = n + 1
				
		elif event.GetId() == 31:
			conn = sqlite3.connect("郵遞區號.db")
			cursor = conn.cursor()
			sql = "SELECT DISTINCT Road FROM tables WHERE City=? and Area=?"
			cursor.execute(sql, [self.edithear1.GetValue(), event.GetString()])
			L = cursor.fetchall()
			self.edithear3.Clear()
			self.edithear4.Clear()
			self.edithear3.SetValue('選擇路段')
			self.edithear4.SetValue('選擇門牌號')
			message1Str = ''
			self.message.SetLabel(message1Str)
			
			n = 0
			for i in range(len(L)):
				t = L[n]
				self.edithear3.Append(t[0])
				n = n + 1
				
		elif event.GetId() == 32:
			conn = sqlite3.connect("郵遞區號.db")
			cursor = conn.cursor()
			sql = "SELECT DISTINCT Scope FROM tables WHERE City=? and Area=? and Road=?"
			cursor.execute(sql, [self.edithear1.GetValue(), self.edithear2.GetValue(), event.GetString()])
			L = cursor.fetchall()
			self.edithear4.Clear()
			self.edithear4.SetValue('選擇門牌號')
			message1Str = ''
			self.message.SetLabel(message1Str)
			
			n = 0
			for i in range(len(L)):
				t = L[n]
				self.edithear4.Append(t[0])
				n = n + 1
				
	def BtnClick(self,event):
		if self.edithear1.GetValue()=='選擇縣市' or self.edithear2.GetValue()=='選擇區' or self.edithear3.GetValue()=='選擇路段' or self.edithear4.GetValue()=='選擇門牌號':
			message1Str = '請輸入完整地址！'
			self.message.SetLabel(message1Str)
		
		elif self.edithear1.GetValue() and self.edithear2.GetValue()and self.edithear3.GetValue()and self.edithear4.GetValue() != '':
			conn = sqlite3.connect("郵遞區號.db")
			cursor = conn.cursor()
			sql = "SELECT Zip5 FROM tables WHERE City=? and Area=? and Road=? and Scope=?"
			cursor.execute(sql, [self.edithear1.GetValue(), self.edithear2.GetValue(), self.edithear3.GetValue(), self.edithear4.GetValue()])
			L = cursor.fetchall()
			
			w = L[0]
			message1Str = '郵遞區號：' + str(w[0])
			self.message.SetLabel(message1Str)
			

				
if __name__ 	== '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()