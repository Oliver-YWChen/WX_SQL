import wx,string,os,wx.grid
import sqlite3 as sqlite

wildcard = "All files (.)|*.*"

class DirDialog(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,title=u"抓取SQLite",size=(940,180))
		panel = wx.Panel(self)
		wx.StaticText(parent=panel,label=u"選擇database：",pos=(10,10))
		self.a = wx.TextCtrl(parent=panel,pos=(100,10),size=(700,23))
		wx.StaticText(parent=panel,label=u"選擇table名稱：",pos=(10,50))
		self.b = wx.TextCtrl(parent=panel,pos=(100,50),size=(700,23))
		self.btn1 = wx.Button(parent=panel,label=u"瀏覽",pos=(810,10))
		self.btn2 = wx.Button(parent=panel,label=u"顯示資料",pos=(810,50))
		
		#新增 BtnClick 事件 -- 開始 --
		self.Bind(wx.EVT_BUTTON,self.BtnClick1,self.btn1)
		self.Bind(wx.EVT_BUTTON,self.BtnClick2,self.btn2)
		
		#新增 BtnClick 事件 -- 結束 --

		
	#撰寫 BtnClick 事件函式 -- 開始 --
	def BtnClick1(self,event):
		dlg = wx.FileDialog(self, u'選擇資料夾', style=wx.DD_DEFAULT_STYLE, wildcard = wildcard)
		if dlg.ShowModal() == wx.ID_OK:
			path = dlg.GetPath()
			self.a.ChangeValue(dlg.GetPath())
			
		dlg.Destroy()
	def BtnClick2(self,event):
	global data
		tn = self.b.GetValue()
		path_o = self.a.GetValue()
		path_e = path_o.split()
		path = ''
		for i in range(len(path_e)-1):
			if i != len(path_e)-2:
				path = path + path_e[i] + '\'
			if i == len(path_e)-2:
				path = path + path_e[i]
		data = path_e[len(path_e)-1]
		os.chdir(path)
		
		class GridFrame(wx.Frame):
			def __init__(self, parent, db):
			global data
				wx.Frame.__init__(self, parent, -1, data)
				grid = wx.grid.Grid(self, -1)
				self.db = db
				self.cur = self.db.con.cursor()
				
				if self.db.exists:
					meta = self.cur.execute("SELECT * from " + self.b.GetValue())
					labels = []
					for i in meta.description:
						labels.append(i[0])
						print(i[0])
					
					result = self.cur.execute("select count(*) from " + self.b.GetValue())
					values = result.fetchone()
					num_rows = values[0]
					
					num_columns = len(labels)
					
					grid.CreateGrid(num_rows, num_columns)
					
					for i in range(num_columns):
						grid.SetColLabelValue(i, labels[i])
						
					# then populate grid with data from DATA
					all = self.cur.execute("SELECT * from " + self.b.GetValue())
					
					count = 0
					for row in all:
						row_num = count
						cells = row[:]
						for i in range(len(cells)):
							if cells[i] != None and cells[i] != "null":
								grid.SetCellValue(row_num, i, str(cells[i]))
						
						count = count + 1
						if count == 100:
							break

		class GetDatabase():
			def __init__(self, f):
				# check db file exists
				try:
					file = open(f)
					file.close()
				except IOError:
					# database doesn't exist - create file & populate it
					self.exists = 0
				else:
					# database already exists - need integrity check here
					self.exists = 1
				self.con = sqlite.connect(f)

		if __name__ == '__main__':
			import sys
			# first open an existing file or create one
			db = GetDatabase(data)
			app = wx.App(0)
			frame = GridFrame(None, db)
			frame.Show(True)
			app.MainLoop()
		
		
	
if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = DirDialog()
	frame.Show()
	app.MainLoop()





class GetDatabase():
	def __init__(self, f):
		# check db file exists
		try:
			file = open(f)
			file.close()
		except IOError:
			# database doesn't exist - create file & populate it
			self.exists = 0
		else:
			# database already exists - need integrity check here
			self.exists = 1
		self.con = sqlite.connect(f)

if __name__ == '__main__':
	import sys
	# first open an existing file or create one
	db = GetDatabase("list.db")
	app = wx.App(0)
	frame = GridFrame(None, db)
	frame.Show(True)
	app.MainLoop()