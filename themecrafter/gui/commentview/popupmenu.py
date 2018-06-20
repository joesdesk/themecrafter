import wx

class PopupMenu(wx.Menu):

    def __init__(self, parent):
        '''Initializes items on menu and binds events.'''
        wx.Menu.__init__(self)
        self.parent = parent
        
        # Probe container structure of comment window
        probe_item = wx.MenuItem(self, wx.NewId(), 'Probe')
        self.Append(probe_item)
        
        