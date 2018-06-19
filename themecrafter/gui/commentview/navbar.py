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
        return True#False
    

class PageNavigbationBar(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
    
        # Page indicator
        self.pagenum_txtctrl = GenStaticText(self, label="")
        
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
        
        # Bind buttons to events
        self.Bind(wx.EVT_BUTTON, self.change_page_by_button)
        
        # Change text to update position
        self.set_page(0, 0)
    
    def AcceptsFocus(self):
        '''Disables this navigation bar from accepting focus.'''
        return True#False
    
    def change_page_by_button(self, event):
        '''Triggers a page change event through a button.'''
        id = event.GetId()
        self.on_change_page(id)
    
    def on_change_page(self, id):
        '''Triggers a page change event.'''
        event = PageChangeEvent(id=id)
        wx.PostEvent(self.GetParent(), event)
        
        #self.GetParent().SetFocusIgnoringChildren()
        return None
        
    def set_page(self, pagenum, totalpages):
        '''Changes the page indicator text.'''
        label = 'Page {:d} of {:d}'.format(pagenum, totalpages)
        self.pagenum_txtctrl.SetLabel(label)
        return None
        
        
def main():
    app = wx.App()
    frame = wx.Frame(None)
    window = PageNavigator(frame)
    window.set_total_pages(10)
    frame.Show()
    app.MainLoop()
    
    
if __name__=='__main__':
    main()
    
    