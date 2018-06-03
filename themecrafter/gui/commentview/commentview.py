import wx

from .commentwindow import CommentWindow
from .navctrl import PageNavigator


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        
        comment_panel = CommentPanel(self)
        
        comment_panel.commentwindow.SetPage('awef')
        #comment_panel = wx.TextCtrl(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(comment_panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        
        #comment_panel.Layout()
    

class CommentView(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.commentwindow = CommentWindow(self, 'awef')
        self.commentwindow.SetPage('awef')
        self.pagenav = PageNavigator(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.commentwindow, 1, wx.ALL|wx.EXPAND, 0)
        sizer.Add(self.pagenav, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        
        self.SetSizer(sizer)
        

if __name__=='__main__':
    
    app = wx.App()
    
    frame = MainFrame(None)
    #sizer = wx.BoxSizer()
    
    
    
    #sizer.Add(comment_panel, 1, wx.GROW, 0)
    #frame.SetSizer(sizer)
    
    #sizer.Fit(frame)
    
    frame.Show()
    
    app.MainLoop()