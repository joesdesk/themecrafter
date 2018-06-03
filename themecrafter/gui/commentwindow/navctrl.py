# Control used to navigate pages

# Controls used
# https://wxpython.org/Phoenix/docs/html/wx.Slider.html
# https://wxpython.org/Phoenix/docs/html/wx.lib.stattext.GenStaticText.html

import wx
from wx.lib.stattext import GenStaticText

class PageNavigator(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        
        self.scrollbar = wx.Slider()
        self.scrollbar.Create(self)
    
        self.pagenum_txtctrl = GenStaticText(self, label="Page 1")
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.pagenum_txtctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer.Add(self.scrollbar, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        
        self.SetSizer(sizer)
        
        # Bind scrolling events
        self.scrollbar.Bind(wx.EVT_SCROLL_CHANGED , self.print_page)
    
    
    def print_page(self, event):
        print('page')
    
    

if __name__=='__main__':
    
    app = wx.App()
    window = PageNavigator(None)
    window.Show()
    app.MainLoop()