#coding:utf-8
import wx,string
class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"薪資試算程式",size=(250,220))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"工作幾年？",pos=(10,10))
		self.a = wx.TextCtrl(parent=panel,value="3",pos=(100,10))
		wx.StaticText(parent=panel,label=u"一個月多少錢？",pos=(10,50))
		self.b = wx.TextCtrl(parent=panel,pos=(100,50))
		self.btn = wx.Button(parent=panel,label=u"結算薪資",pos=(10,100))
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn)
		#新增 BtnClick 事件 -- 結束 --
		self.message1 = wx.StaticText(parent=panel,pos=(10,130))
		self.message2 = wx.StaticText(parent=panel,pos=(10,160))
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		a = self.a.GetValue()
		a = float(a)
		b = self.b.GetValue()
		b = float(b)
		c = b * 12 * a
		d = c /(365 * a)
		message1Str = u'您工作 '+str(a)+u' 年可以獲得 '+str(c)+u' 元'
		message2Str = u'平均每日獲得 '+str(d)+u' 元'
		self.message1.SetLabel(message1Str)
		self.message2.SetLabel(message2Str)
		self.b.ChangeValue('')
	#撰寫 BtnClick 事件函式 -- 結束 --
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()