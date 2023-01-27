def mediaBrowse(self, event):
	dialog = wx.DirDialog(self, 'Choose media directory', '',style=wx.DD_DEFAULT_STYLE)
	try:
		if dialog.ShowModal() == wx.ID_CANCEL:
			return
		path = dialog.GetPath()
	except Exception:
		wx.LogError('Failed to open directory!')
		raise
	finally:
		dialog.Destroy()
	
	if len(path) > 0:
		self.mediaPathTextCtrl.SetValue(path)
		self.pg.mplayer.setCWD(path) 