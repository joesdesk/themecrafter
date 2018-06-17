# Sources:
# Closing frame. http://zetcode.com/wxpython/menustoolbars/

import wx
from .menubar import MenuBar


class MainFrame(wx.Frame):
    '''Base for the main application frame.'''
    
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY, title='ThemeCrafter v0.0', size=(500,400))
        
        # Add the main menubar
        menubar = MenuBar()
        self.SetMenuBar(menubar)
        
        # Frame specific bindings
        self.Bind(wx.EVT_MENU, self.Quit, id=wx.ID_EXIT)
        
        
    def Quit(self, e):
        '''Closes the frame.'''
        self.Close()