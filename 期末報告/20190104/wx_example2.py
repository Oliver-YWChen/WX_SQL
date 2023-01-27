# -*- coding: utf-8 -*-

# A full example
# https://wiki.wxpython.org/wxPython%20by%20Example

#-------------------------------------------------------------------------------
#   <<project>>
# 
#-------------------------------------------------------------------------------

import wx, wx.html
import sys

# 訊息視窗的文字內容
aboutText = """<p>抱歉，沒有關於這個程式的資訊 Sorry, there is no information about this program. It is
running on version %(wxpy)s of <b>wxPython</b> and %(python)s of <b>Python</b>.
See <a href="http://wiki.wxpython.org">wxPython Wiki</a></p>""" 

class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()

    def OnLinkClicked(self, link):
        wx.LaunchDefaultBrowser(link.GetHref())
        
class AboutBox(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "About <<project>>",
            #style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
            style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL)
        hwin = HtmlWindow(self, -1, size=(400,200))
        vers = {}
        vers["python"] = sys.version.split()[0]
        vers["wxpy"] = wx.VERSION_STRING
        hwin.SetPage(aboutText % vers)
        btn = hwin.FindWindowById(wx.ID_OK)
        irep = hwin.GetInternalRepresentation()
        hwin.SetSize((irep.GetWidth()+25, irep.GetHeight()+10))
        self.SetClientSize(hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()

class Frame(wx.Frame):
    def __init__(self, title):
        # 設定視窗的 title, pos, size
        wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(350,200))
        
        # 設定當視窗被關閉時 (發生 EVT_CLOSE 事件)，將呼叫 OnClose() 函式
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # 建立選單列 MenuBar
        menuBar = wx.MenuBar()
        
        menu = wx.Menu()    # 新增一個選單 Menu
        
        # 在選單中加入選項
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)  # 綁定選項對應的函式 OnClose()
        
        # 將選單加入選單列中，並且設定快速鍵 ALT-F
        menuBar.Append(menu, "&File")
        
        menu = wx.Menu()    # 新增一個選單 Menu
        
        # 在選單中加入選項
        m_about = menu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, m_about) # 綁定選項對應的函式 OnAbout()
        
        # 將選單加入選單列中，並且設定快速鍵 ALT-H
        menuBar.Append(menu, "&Help")
        self.SetMenuBar(menuBar)
        
        # 建立狀態列 StatusBar
        self.statusbar = self.CreateStatusBar()
        
        # 建立面板
        panel = wx.Panel(self)
        
        # 建立 BoxSizer 物件
        # BoxSizer 的用法：
        # https://wxpython.org/Phoenix/docs/html/sizers_overview.html#programming-with-boxsizer
        # http://stanley2910.pixnet.net/blog/post/147824333
        #
        box = wx.BoxSizer(wx.VERTICAL)
        
        # 加入標籤文字 StaticText，並且設定字型和大小
        m_text = wx.StaticText(panel, -1, "Hello World!")
        m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        m_text.SetSize(m_text.GetBestSize())
        
        # 加入 box 中
        box.Add(m_text, 0, wx.ALL, 10)
        
        # 建立 Close 按鈕
        m_close = wx.Button(panel, wx.ID_CLOSE, "Close")
        m_close.Bind(wx.EVT_BUTTON, self.OnClose) # 綁定選項對應的函式 OnClose()
        box.Add(m_close, 0, wx.ALL, 10) # 加入 box 中
        
        # 設定面板
        panel.SetSizer(box)
        panel.Layout()

    def OnClose(self, event):
        # 產生訊息視窗
        dlg = wx.MessageDialog(self, 
            "Do you really want to close this application?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        
        # 顯示訊息視窗
        result = dlg.ShowModal()
        dlg.Destroy()   # 關閉視窗
        if result == wx.ID_OK:  # 檢查是否按了 [確定]
            self.Destroy()

    def OnAbout(self, event):
        # 建立 About 對話視窗
        dlg = AboutBox()
        dlg.ShowModal() # 顯示視窗
        dlg.Destroy()  

# 建立 APP
app = wx.App(redirect=True)   # Error messages go to popup window

# 建立一個視窗，視窗的標題是 Example
top = Frame("Example")

top.Show()  # 顯示視窗
app.MainLoop()