import wx

class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None)


if __name__=='__main__':
    app = wx.App()
    mainwindow = MainWindow()
    mainwindow.Show()
    app.MainLoop()
