import wx

from .commentwindow import CommentWindow
from .navctrl import PageNavigator, EVT_PAGE_CHANGE

from ...output.html2 import HTMLTransform


class CommentView(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Data to view by the widget
        self.xmlstring = ''
        
        # Control components
        self.commentwindow = CommentWindow(self)
        self.pagenav = PageNavigator(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.commentwindow, 1, wx.EXPAND, 0)
        sizer.Add(self.pagenav, 0, wx.EXPAND, 0)
        
        self.SetSizer(sizer)
        
        # Page events
        self.Bind(EVT_PAGE_CHANGE, self.on_page_change)
        self.Bind(wx.EVT_KEY_DOWN, self.on_shift_page)
        
    def set_data(self, xmlstring):
        self.html = HTMLTransform(xmlstring)
        n_pages = self.html.paginate(10)
        self.pagenav.set_total_pages(n_pages)
        self.set_page(1)
    
    def on_page_change(self, event):
        page = event.page
        self.set_page(page)
        
    def on_shift_page(self, event):
        keycode = event.GetKeyCode()
        page = self.pagenav.pagenum
        if keycode==wx.WXK_LEFT:
            page = self.pagenav.set_page(page-1)
            self.set_page(page)
        if keycode==wx.WXK_RIGHT:
            page = self.pagenav.set_page(page+1)
            self.set_page(page)
            
    def set_page(self, page):
        text = self.html.show_page(page)
        self.commentwindow.SetPage(text)
            
            
if __name__=='__main__':
    
    from ...nlp.session import PreprocessingSession
    
    session = PreprocessingSession()
    session.open_tree('try.xml')
    xmlstring = session.tree_as_string()
    
    app = wx.App()
    frame = wx.Frame(None)
    
    comment_panel = CommentView(frame)
    comment_panel.set_data(xmlstring)
    frame.Show()
    
    app.MainLoop()