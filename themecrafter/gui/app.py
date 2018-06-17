import wx
from .appframe import ApplicationFrame

class Application:
    '''Container for the application'''

    def __init__(self):
        pass
        
    def start(self):
        app = wx.App()
        frame = ApplicationFrame()
        frame.Show()
        app.MainLoop()
        
        