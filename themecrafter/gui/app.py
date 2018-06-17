import wx


class Application:
    '''Container for the application'''

    def __init__(self):
        pass
        
    def start(self):
        app = wx.App()
        frame = MainFrame()
        frame.Show()
        app.MainLoop()
        
        
class MainFrame(wx.Frame):
    '''Uses the mainwindow as a base for the main application window.'''
    
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='ThemeCrafter v0.0')
        
    