import wx

from .commentwindow import CommentWindow
from .navctrl import PageNavigator


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
    frame = wx.Frame(None)
    
    comment_panel = CommentView(frame)
    frame.Show()
    
    app.MainLoop()