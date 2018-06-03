import wx

from .commentwindow import CommentWindow
from .navctrl import PageNavigator

from ...output.html2 import HTMLTransform


class CommentView(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Data to view by the widget
        self.xmlstring = ''
        
        self.commentwindow = CommentWindow(self, 'awef')
        self.commentwindow.SetPage('awef')
        self.pagenav = PageNavigator(self)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.commentwindow, 1, wx.ALL|wx.EXPAND, 0)
        sizer.Add(self.pagenav, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        
        self.SetSizer(sizer)
        
        # Page navigation events
        self.pagenav.Bind(wx.EVT_SCROLL_CHANGED, self.set_page)
        
    def set_data(self, xmlstring):
        self.html = HTMLTransform(xmlstring)        
    
    def set_page(self, event):
        page = self.pagenav.scrollbar.GetValue()
        txt = self.html.render(self.html.docs[page:page+1], rename_tags=True)
        self.commentwindow.SetPage(txt)
    

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