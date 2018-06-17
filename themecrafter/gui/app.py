import wx


class Application:

    def __init__(self):
        pass
        
    def start(self):
        app = wx.App()
        frame = wx.Frame(None)
        frame.Show()
        app.MainLoop()
        
        