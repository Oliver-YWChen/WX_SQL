# a demonstration of wxPython's grid with various functions, and linked to SQLite
# (c) 2014 Alan James Salmoni. Released under the Lesser GPL license.

import wx
import wx.grid
import sqlite3 as sqlite

import string

class GridFrame(wx.Frame):
    def __init__(self, parent, db):
        wx.Frame.__init__(self, parent, -1, "wxPython Grid & SQLite Demo")
        
        # Create a wxGrid object
        grid = wx.grid.Grid(self, -1)
        
        self.db = db
        self.cur = self.db.con.cursor()
        
        if self.db.exists:
            # read labels in from DATA table
            meta = self.cur.execute("SELECT * from photos")
            labels = []
            for i in meta.description:
                labels.append(i[0])
                #print(i[0])
            
            # calculate number of columns            
            num_columns = len(labels)
            
            # select all records from the table
            all = self.cur.execute("SELECT * from photos ORDER by IMAGE_NAME")
            
            
            # calculate number of rows
            result = self.cur.execute("select count(*) from photos")            
            values = result.fetchone()
            num_rows = values[0]
            print("number of rows: %d" % num_rows)
            
            # Then we call CreateGrid to set the dimensions of the grid
            grid.CreateGrid(num_rows, num_columns)
            
            # set column labels
            for i in range(num_columns):
                grid.SetColLabelValue(i, labels[i])
                
            # select all records from the table
            all = self.cur.execute("SELECT * from photos ORDER by IMAGE_NAME")
            
            # then populate grid with data from DATA
            count = 0
            for row in all:
                row_num = count
                cells = row[:]
                for i in range(len(cells)):
                    if cells[i] != None and cells[i] != "null":
                        grid.SetCellValue(row_num, i, str(cells[i]))
                
                count = count + 1
        
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
    db = GetDatabase("db01.db")
    app = wx.App(0)
    frame = GridFrame(None, db)
    frame.Show(True)
    app.MainLoop()