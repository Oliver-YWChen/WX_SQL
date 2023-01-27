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
        
        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        grid.CreateGrid(100, 10)

        self.db = db
        self.cur = self.db.con.cursor()
        
        if self.db.exists:
            # read labels in from DATA table
            meta = self.cur.execute("SELECT * from photos")
            labels = []
            for i in meta.description:
                labels.append(i[0])
                print(i[0])
            
            # calculate number of columns            
            num_columns = len(labels)
            
            # set column labels
            #for i in range(num_columns):
            for i in range(10):
                grid.SetColLabelValue(i, labels[i])
                
            # then populate grid with data from DATA
            all = self.cur.execute("SELECT * from photos ORDER by IMAGE_NAME")
            count = 0
            for row in all:
                row_num = count
                cells = row[:]
                #for i in range(len(cells)):
                for i in range(10):
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
    db = GetDatabase("db01.db")
    app = wx.App(0)
    frame = GridFrame(None, db)
    frame.Show(True)
    app.MainLoop()