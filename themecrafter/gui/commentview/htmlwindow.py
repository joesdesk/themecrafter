import wx
import wx.html

from .container_utils import parse
from .popupmenu import PopupMenu

# Depreciated: Format using HTML instead of custom tags
# from .taghandlers import DocumentTagHandler, TokenTagHandler
#wx.html.HtmlWinParser_AddTagHandler(DocumentTagHandler)
#wx.html.HtmlWinParser_AddTagHandler(TokenTagHandler)


class HtmlWindow(wx.html.HtmlWindow):
    '''A small widget to view html formatted comments.'''
    
    def __init__(self, parent):
        wx.html.HtmlWindow.__init__(self, parent)

        if "gtk2" in wx.PlatformInfo or "gtk3" in wx.PlatformInfo:
            self.SetStandardFonts()

        self.ShowScrollbars(wx.SHOW_SB_NEVER, wx.SHOW_SB_DEFAULT)
        #self.EnableScrolling(False, wx.VSCROLL)
        #self.StopAutoScrolling()
        
        self.parser = self.GetParser()
        #print(self.parser)
        
        self.htmlstring = ''
        
        # This gives segmentation fault
        #parser_prod = self.parser.GetProduct()

        # Depreciated: No events associated with hovering over cells
        #self.Bind(wx.html.EVT_HTML_CELL_HOVER, self.hightlight_hover)
        #self.Bind(wx.html.EVT_HTML_CELL_CLICKED, self.check_format)
        #self.Bind(DATA_LOAD, self.show_data)

        # Depreciated: Page change event by keypress will be caught by parent
        #self.Bind(wx.EVT_KEY_DOWN, self.CatchHKeyScroll)
        self.Bind(wx.EVT_KEY_UP, self.CatchHKeyScroll)
        
        # Right click to see option to print container structure
        self.Bind(wx.EVT_RIGHT_DOWN, self.show_popup)
        
        
    def AcceptsFocus(self):
        '''Disables this control from accepting focus.'''
        return True#False
        
    def hightlight_hover(self, event):
        '''Test to see if hovering over cells allows highlighting.'''
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
        '''Test to see if displaying the page works.'''
        #print("event detected")
        #self.SetPage("""<html> A concordance is more than an index;
        #additional material make producing them a labor-intensive process,
        #even when assisted by computers, such as commentary, definitions,
        #and topical cross-indexing.</html>""")
        pass
    
    def check_format(self):
        '''Probes the structure of the comment window for diagnosing problems.'''
        print("format detected")
        
        container = self.GetInternalRepresentation()
        parse(container, lvl=0)
        
        #self.Refresh()
        #print("Done")
        pass
        
    def CatchHKeyScroll(self, event):
        '''Disables horizontal key presses from scrolling horizontally.'''
        print('window caught keypress')
        keycode = event.GetKeyCode()
        # See: https://wxpython.org/Phoenix/docs/html/wx.KeyCategoryFlags.enumeration.html#wx-keycategoryflags
        if event.IsKeyInCategory(wx.WXK_CATEGORY_ARROW):
            # See: https://wxpython.org/Phoenix/docs/html/wx.KeyEvent.html#wx.KeyEvent.GetKeyCode
           
            
            # See: https://wxpython.org/Phoenix/docs/html/wx.KeyCode.enumeration.html#wx-keycode
            if (keycode==wx.WXK_LEFT) or (keycode==wx.WXK_RIGHT):
                event.Skip()
                return None
        
        event.Skip()
    
    def load_page(self, htmlstring):
        self.SetPage(htmlstring)
        self.htmlstring = htmlstring
        
    def show_popup(self, event):
        '''Shows the popup menu'''
        popupmenu = PopupMenu(self)
        popupmenu.Bind(wx.EVT_MENU, self.on_popupmenu_sel)
        self.PopupMenu(popupmenu, event.GetPosition())
        # Must be destroyed after use
        popupmenu.Destroy()
        
    def on_popupmenu_sel(self, event):
        '''Handles events from seleting an item on the popup menu.'''
        print(event.GetId())
        self.check_format()
        
        