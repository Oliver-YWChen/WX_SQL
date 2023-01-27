#coding:utf-8
import wx,string
class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"Buffer",size=(670,280))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"Input:",pos=(10,10))
		self.a = wx.TextCtrl(parent=panel,value="",pos=(10,30),size=(530,23))
		wx.StaticText(parent=panel,label=u"Output folder",pos=(10,55))
		self.b = wx.TextCtrl(parent=panel,pos=(10,75),size=(530,23))
		wx.StaticText(parent=panel,label=u"Name:",pos=(10,100))
		self.c = wx.TextCtrl(parent=panel,pos=(10,120))
		wx.StaticText(parent=panel,label=u"Distance(meter):",pos=(10,145))
		self.d = wx.TextCtrl(parent=panel,pos=(10,165))
		
		self.btn1 = wx.Button(parent=panel,label=u"瀏覽",pos=(550,30))
		self.btn2 = wx.Button(parent=panel,label=u"瀏覽",pos=(550,75))
		self.btn3 = wx.Button(parent=panel,label=u"確認",pos=(10,200))
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick1,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick2,self.btn2)
		self.Bind(wx.EVT_BUTTON,self.BtnClick3,self.btn3)
		#新增 BtnClick 事件 -- 結束 --

	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick1(self,event):
		dlg = wx.DirDialog(self,u"選擇資料夾",style=wx.DD_DEFAULT_STYLE)
		if dlg.ShowModal() == wx.ID_OK:
			print(dlg.GetPath())
		dlg.Destroy()
		
	def BtnClick2(self,event):
		print ("Event handler 'button_browse_path_click' not implemented!")
		dlg = wx.DirDialog(self,"Choose a directory:",style=wx.DD_DEFAULT_STYLE)

		if dlg.ShowModal() == wx.ID_OK:
			self.text_ctrl_outpath.Clear()
			self.text_ctrl_outpath.SetValue(dlg.GetPath())
			print('You selected: %s\n' % dlg.GetPath())
		dlg.Destroy()
		event.Skip()

	def BtnClick3(self,event):
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