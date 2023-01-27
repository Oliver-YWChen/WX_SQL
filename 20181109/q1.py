#coding:utf-8
import wx,string
class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"閏年判斷",size=(250,220))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"請輸入年份",pos=(10,10))
		self.a = wx.TextCtrl(parent=panel,value="",pos=(100,10))
		self.btn1 = wx.Button(parent=panel,label=u"確定",pos=(10,50))
		self.btn2 = wx.Button(parent=panel,label=u"清除",pos=(100,50))
		
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick_c,self.btn2)
		
		#新增 BtnClick 事件 -- 結束 --
		self.message = wx.StaticText(parent=panel,pos=(10,130))
		
		
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		a = self.a.GetValue()
		a = int(a)
		if a%4 != 0:
			w = '不是閏年!'
		elif a%100 != 0:
			w = '是閏年!'
		elif a%400 != 0:
			w = '不是閏年!'
		elif a%400 == 0:
			w = '是閏年!'
		message1Str = str(w)
		self.message.SetLabel(message1Str)
		
	def BtnClick_c(self,event):
		self.a.ChangeValue('')
		
	#撰寫 BtnClick 事件函式 -- 結束 --
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()