# Creating menus

# Menu for the application and user files
filemenu = wx.Menu()
filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program.")
filemenu.AppendSeparator()
filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program.")
self.Append(filemenu, "File")

# Menu for the editing process
editmenu = wx.Menu()
editmenu.Append(wx.ID_ANY, "Undo")
editmenu.Append(wx.ID_ANY, "Redo")
self.Append(editmenu, "Edit")

# Menu for the data loading process
datamenu = wx.Menu()
datamenu.Append(wx.ID_ANY, "Load Docs from csv")
self.Append(datamenu, "Data")
