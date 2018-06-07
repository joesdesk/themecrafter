import wx

from .commentwindow import CommentWindow
from .navctrl import PageNavigator, EVT_PAGE_CHANGE


class CommentView(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Data to view by the widget
        self.htmlpages = None
        
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
        
    def set_data(self, htmlpages):
        self.htmlpages = htmlpages
        n_pages = len(htmlpages)
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
        if self.htmlpages is not None:
            text = self.htmlpages[page]
            self.commentwindow.SetPage(text)
            
            internal = self.commentwindow.GetInternalRepresentation()
            #print(internal)
            #self.parse(internal)
            
    
    def parse(self, container, lvl=0):
        if container is None:
            pass
            #print('    '*lvl + 'None')
        #elif lvl>=2:
        #    pass
        else:
            
            if str(type(container))==r"<class 'wx._html.HtmlContainerCell'>":
                bgcolor = container.GetBackgroundColour()
                halign = container.GetAlignHor()
                valign = container.GetAlignVer()
                print('    '*lvl + str(bgcolor) + str(halign) + str(valign) )
            elif str(type(container))==r"<class 'wx._html.HtmlWordCell'>":
                #textrep = container.word
                print('    '*lvl + str('HTML_WORD_CELL') )
            else:
                print('    '*lvl + str(type(container)) )
            
            self.parse(container.GetFirstChild(), lvl+1)
            self.parse(container.GetNext(), lvl)
    
            
if __name__=='__main__':
    
    #from ...nlp.session import PreprocessingSession
    
    #session = PreprocessingSession()
    #session.open_tree('try.xml')
    #xmlstring = session.tree_as_string()
    
    app = wx.App()
    frame = wx.Frame(None)
    
    comment_panel = CommentView(frame)
    #comment_panel.set_data(xmlstring)
    frame.Show()
    
    app.MainLoop()