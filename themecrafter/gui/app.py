import wx
from .mainframe.mainframe import MainFrame

class Application:
    '''Container for the application'''

    def __init__(self):
        pass
        
    def start(self):
        app = wx.App()
        frame = MainFrame()
        frame.Show()
        app.MainLoop()
        
        