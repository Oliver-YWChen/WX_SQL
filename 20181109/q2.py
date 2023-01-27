#coding:utf-8
import wx,string
class MySalgar(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"成績計算",size=(250,300))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"請輸入國文成績",pos=(10,10))
		self.ch = wx.TextCtrl(parent=panel,value="",pos=(100,10))
		wx.StaticText(parent=panel,label=u"請輸入數學成績",pos=(10,50))
		self.ma = wx.TextCtrl(parent=panel,value="",pos=(100,50))
		wx.StaticText(parent=panel,label=u"請輸入英文成績",pos=(10,90))
		self.eng = wx.TextCtrl(parent=panel,value="",pos=(100,90))
		
		self.btn1 = wx.Button(parent=panel,label=u"確定",pos=(10,130))
		self.btn2 = wx.Button(parent=panel,label=u"清除",pos=(100,130))
		
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick_c,self.btn2)
		
		#新增 BtnClick 事件 -- 結束 --
		self.message1 = wx.StaticText(parent=panel,pos=(10,170))
		self.message2 = wx.StaticText(parent=panel,pos=(10,210))
		
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick(self,event):
		ch = self.ch.GetValue()
		ch = float(ch)
		ma = self.ma.GetValue()
		ma = float(ma)
		eng = self.eng.GetValue()
		eng = float(eng)
		avr = (ch + ma + eng)/3
		
		if 80 <= avr <= 100:
			w = '非常好!'
		elif 70 <= avr <= 79:
			w = '很好!'
		elif 60 <= avr <= 69:
			w = '普通!'
		elif avr < 60:
			w = '要加油喔!'
		
		message1Str = u'平均:'+str(avr)
		message2Str = str(w)
		self.message1.SetLabel(message1Str)
		self.message2.SetLabel(message2Str)
		
	def BtnClick_c(self,event):
		self.ch.ChangeValue('')
		self.ma.ChangeValue('')
		self.eng.ChangeValue('')
		
	#撰寫 BtnClick 事件函式 -- 結束 --
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = MySalgar()
	frame.Show()
	app.MainLoop()