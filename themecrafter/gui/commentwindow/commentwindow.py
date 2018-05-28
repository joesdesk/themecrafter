import wx
import wx.html

from .taghandlers import CommentTagHandler, TokenTagHandler

wx.html.HtmlWinParser_AddTagHandler(CommentTagHandler)
wx.html.HtmlWinParser_AddTagHandler(TokenTagHandler)


class CommentWindow(wx.html.HtmlWindow):
    '''A small widget to view html formatted comments.'''
    
    def __init__(self, parent, title):
        wx.html.HtmlWindow.__init__(self, parent)

        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            self.SetStandardFonts()

        self.ShowScrollbars(wx.SHOW_SB_NEVER, wx.SHOW_SB_DEFAULT)
        #self.EnableScrolling(False, wx.VSCROLL)
        #self.StopAutoScrolling()
        
        self.parser = self.GetParser()
        #print(self.parser)
        
        # This gives segmentation fault
        #parser_prod = self.parser.GetProduct()
        
        

        #self.Bind(wx.html.EVT_HTML_CELL_HOVER, self.hightlight_hover)
        self.Bind(wx.html.EVT_HTML_CELL_CLICKED, self.check_format)
        #self.Bind(DATA_LOAD, self.show_data)

        self.Bind(wx.EVT_KEY_DOWN, self.CatchHKeyScroll)
        #self.Bind(wx.EVT_KEY_UP, self.CatchHKeyScroll)
        
        
    def hightlight_hover(self, event):
        cell = event.GetCell()#.GetNext()
        if (cell is not None) and (cell != ''):
            cid = cell.GetId()
            if cid != '':
                print(cid)

        #self.update_counts += 1
        #print(self.update_counts)

        #self.SetPage("""<html><body width="200px"> A concordance is more than an index;
        #additional material make producing them a labor-intensive process,
        #even when assisted by computers, such as commentary, definitions,
        #and topical cross-indexing.
        #""" +
        #str(self.update_counts) +
        #"</body></html>")
        
        # if self.page1:
            # self.SetPage(page2)
            # self.page1 = False
            # self.Refresh()
        # else:
            # self.SetPage(page)
            # self.page1  = True
            # self.Refresh()
        # print(self.page1)
        #c = event.GetCell().GetParent()
        #print(event.GetCell().GetParent())
        #self.GetParser().
        #c.SetBackgroundColour("#e7e7e7")
        #sprint(c.GetBackgroundColour())
        #c.SetLabel("aewf")
        #self.Refresh()
        #print(c)

        #c.Draw()
    
    def show_data(self, event):
        print("event detected")
        self.SetPage("""<html> A concordance is more than an index;
        additional material make producing them a labor-intensive process,
        even when assisted by computers, such as commentary, definitions,
        and topical cross-indexing.</html>""")
        
    
    def check_format(self, event):
        print("format detected")
        
        container = self.GetInternalRepresentation()
        self.list_children(container, lvl=0)
        
        
        
        
        #
        
        self.Refresh()
        

        #print("Done")


    def list_children(self, container, lvl):
        '''Returns the next child.'''
        
        #print(lvl)
        
        next_container = container.GetFirstChild()
        while next_container is not None:
            
            if type(next_container)==wx.html.HtmlContainerCell:
                next_container.SetBackgroundColour("#BBBBBB")
                next_container.SetWidthFloat(20, wx.html.HTML_UNITS_PIXELS)
                id = next_container.GetId()
                #print(id)
                
                #next_container.SetBorder("#BBBBBB", "#BBBBBB", 2)
            
            self.list_children(next_container, lvl+1)
            next_container = next_container.GetNext()
    
    
    def CatchHKeyScroll(self, event):
        '''Disables horizontal key presses from scrolling horizontally.'''
        
        # See: https://wxpython.org/Phoenix/docs/html/wx.KeyCategoryFlags.enumeration.html#wx-keycategoryflags
        if event.IsKeyInCategory(wx.WXK_CATEGORY_ARROW):
            # See: https://wxpython.org/Phoenix/docs/html/wx.KeyEvent.html#wx.KeyEvent.GetKeyCode
            keycode = event.GetKeyCode()
            
            # See: https://wxpython.org/Phoenix/docs/html/wx.KeyCode.enumeration.html#wx-keycode
            if keycode==wx.WXK_LEFT:
                return None
            
            if keycode==wx.WXK_RIGHT:
                return None
            
        event.Skip()
    
