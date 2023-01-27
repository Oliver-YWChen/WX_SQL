import wx,wx.grid,string
import sqlite3 as sqlite
import sqlite3

class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"成績計算",size=(250,300))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"請輸入學號",pos=(10,10))
		self.num = wx.TextCtrl(parent=panel,value="",pos=(100,10))
		wx.StaticText(parent=panel,label=u"請輸入姓名",pos=(10,50))
		self.name = wx.TextCtrl(parent=panel,value="",pos=(100,50))
		wx.StaticText(parent=panel,label=u"請輸入平時成績",pos=(10,90))
		self.g = wx.TextCtrl(parent=panel,value="",pos=(100,90))
		wx.StaticText(parent=panel,label=u"請輸入出席率",pos=(10,130))
		self.p = wx.TextCtrl(parent=panel,value="",pos=(100,130))
		
		self.btn1 = wx.Button(parent=panel,label=u"插入",pos=(10,170))
		self.btn2 = wx.Button(parent=panel,label=u"清除",pos=(100,170))

		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick_c,self.btn2)
		
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		num = str(self.num.GetValue())
		name = str(self.name.GetValue())
		g = str(self.g.GetValue())
		p = str(self.p.GetValue())
		
		conn = sqlite3.connect("list.db")
		cursor = conn.cursor()
		albums_entry = [(num, name, g ,p)]
		cursor.executemany("INSERT INTO student VALUES (?,?,?,?)", albums_entry)
		conn.commit()
		
	def BtnClick_c(self,event):
		self.num.ChangeValue('')
		self.name.ChangeValue('')
		self.g.ChangeValue('')
		self.p.ChangeValue('')
		
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()
	

