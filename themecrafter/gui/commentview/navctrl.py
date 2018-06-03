# Control used to navigate pages

# Controls used
# https://wxpython.org/Phoenix/docs/html/wx.Slider.html
# https://wxpython.org/Phoenix/docs/html/wx.lib.stattext.GenStaticText.html

import wx
from wx.lib.stattext import GenStaticText

class PageNavigator(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.scrollbar = wx.Slider()
        self.scrollbar.Create(self)
    
        self.pagenum_txtctrl = GenStaticText(self, label="Page 1")
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.pagenum_txtctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer.Add(width=10, height=0)
        sizer.Add(self.scrollbar, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        
        self.SetSizer(sizer)
        
        # Bind scrolling events
        self.scrollbar.Bind(wx.EVT_SCROLL_CHANGED , self.print_page)
    
    
    def print_page(self, event):
        page_num = self.scrollbar.GetValue()
        txt = "Page " + str(page_num)
        self.pagenum_txtctrl.SetLabel(txt)
        
    

if __name__=='__main__':
    
    app = wx.App()
    window = PageNavigator(None)
    window.Show()
    app.MainLoop()