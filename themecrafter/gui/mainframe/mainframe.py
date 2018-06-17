import wx


class MainFrame(wx.Frame):
    '''Uses the mainwindow as a base for the main application window.'''
    
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title='ThemeCrafter v0.0', size=(500,400))
        
        