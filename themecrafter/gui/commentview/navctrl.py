# Control used to navigate pages

# Controls used
# https://wxpython.org/Phoenix/docs/html/wx.Slider.html
# https://wxpython.org/Phoenix/docs/html/wx.lib.stattext.GenStaticText.html

import wx
import wx.lib.newevent
from wx.lib.stattext import GenStaticText


# Create event for page change.
PageChangeEvent, EVT_PAGE_CHANGE = wx.lib.newevent.NewCommandEvent()

# IDs associated with the buttons
ID_FIRST = 50
ID_PREV = 51
ID_NEXT = 52
ID_LAST = 53


class NavButton(wx.Button):

    def __init__(self, parent, id, label):
        width = 60
        wx.Button.__init__(self, parent, id, label, size=(width, -1))

    def AcceptsFocus(self):
        '''Disables this control from accepting focus.'''
        return False
    

class PageNavigator(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
    
        # Page indicator
        self.pagenum_txtctrl = GenStaticText(self, label="Page 1 of 1")
        
        # Page controls
        width = 60
        self.first_btn = NavButton(self, id=ID_FIRST, label='First')
        self.prev_btn = NavButton(self, id=ID_PREV, label='Previous')
        self.next_btn = NavButton(self, id=ID_NEXT, label='Next')
        self.last_btn = NavButton(self, id=ID_LAST, label='Last')

        
        # Arranging layout
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        sizer.AddSpacer(1)
        sizer.Add(self.first_btn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)
        sizer.AddSpacer(1)
        sizer.Add(self.prev_btn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)
        
        sizer.AddStretchSpacer(1)
        sizer.Add(self.pagenum_txtctrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)
        sizer.AddStretchSpacer(1)
        
        sizer.Add(self.next_btn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)
        sizer.AddSpacer(1)
        sizer.Add(self.last_btn, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0)
        sizer.AddSpacer(1)
        
        self.SetSizer(sizer)
        
        # Internal variable
        self.pagenum = 1
        self.n_pages = 1
        
        # Bind buttons to events
        self.Bind(wx.EVT_BUTTON, self.change_page)
    
    def AcceptsFocus(self):
        '''Disables this navigation bar from accepting focus.'''
        return False
    
    def change_page(self, event):        
        id = event.GetId()
        if id==ID_FIRST:
            page = self.set_page(1)
        elif id==ID_PREV:
            page = self.set_page(self.pagenum-1)
        elif id==ID_NEXT:
            page = self.set_page(self.pagenum+1)
        elif id==ID_LAST:
            page = self.set_page(self.n_pages)
        else:
            return None
            
        event = PageChangeEvent(id=id, page=page)
        wx.PostEvent(self.GetParent(), event)
        
        self.GetParent().SetFocusIgnoringChildren()
        return None
    
    def set_page(self, pagenum):
        # Coerce to within number of pages
        if pagenum < 1:
            return 1
        if pagenum > self.n_pages:
            return self.n_pages
        
        self.pagenum = pagenum
        
        label = 'Page {:d} of {:d}'.format(pagenum, self.n_pages)
        self.pagenum_txtctrl.SetLabel(label)
        return pagenum
        
    def set_total_pages(self, n):
        self.n_pages = n
        self.set_page(self.pagenum)
        

if __name__=='__main__':
    
    app = wx.App()
    frame = wx.Frame(None)
    window = PageNavigator(frame)
    window.set_total_pages(10)
    frame.Show()
    app.MainLoop()