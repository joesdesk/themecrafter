import wx

from .htmlwindow import HtmlWindow
from .navbar import PageNavigbationBar

from .navbar import PageChangeEvent, EVT_PAGE_CHANGE
from .navbar import ID_FIRST, ID_PREV, ID_NEXT, ID_LAST


class MainPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Panel components
        self.commentwindow = HtmlWindow(self)
        self.pagenav = PageNavigbationBar(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.commentwindow, 1, wx.EXPAND, 0)
        sizer.Add(self.pagenav, 0, wx.EXPAND, 0)
        
        self.SetSizer(sizer)
        
        # Page events
        self.commentwindow.Bind(wx.EVT_KEY_DOWN, self.change_page_by_key)
        
    def change_page_by_key(self, event):
        print('keypress')
        keycode = event.GetKeyCode()
        if keycode==wx.WXK_LEFT:
            self.pagenav.on_change_page(id=ID_PREV)
            return None
        if keycode==wx.WXK_RIGHT:
            self.pagenav.on_change_page(id=ID_NEXT)
            return None
        event.Skip()
            
if __name__=='__main__':
    
    app = wx.App()
    frame = wx.Frame(None)
    
    comment_panel = CommentView(frame)
    #comment_panel.set_data(xmlstring)
    frame.Show()
    
    app.MainLoop()