import wx,wx.grid,string
import sqlite3 as sqlite
class GridFrame(wx.Frame):
	def __init__(self, parent, db):
		wx.Frame.__init__(self, parent, -1, "list")
		grid = wx.grid.Grid(self, -1)
		self.db = db
		self.cur = self.db.con.cursor()
		
		if self.db.exists:
			meta = self.cur.execute("SELECT * from student")
			labels = []
			for i in meta.description:
				labels.append(i[0])
				print(i[0])
			
			result = self.cur.execute("select count(*) from student")
			values = result.fetchone()
			num_rows = values[0]
			
			num_columns = len(labels)
			
			grid.CreateGrid(num_rows, num_columns)
			
			for i in range(num_columns):
				grid.SetColLabelValue(i, labels[i])
				
			# then populate grid with data from DATA
			all = self.cur.execute("SELECT * from student")
			
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
	db = GetDatabase("list.db")
	app = wx.App(0)
	frame = GridFrame(None, db)
	frame.Show(True)
	app.MainLoop()
		