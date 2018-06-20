import wx

ID_PROBE_CONTAINER = 100
ID_PROBE_XML = 101


class PopupMenu(wx.Menu):

    def __init__(self, parent):
        '''Initializes items on menu and binds events.'''
        wx.Menu.__init__(self)
        self.parent = parent
        
        # Print container structure of comment window
        probe_container_item = wx.MenuItem(self, id=ID_PROBE_CONTAINER, text='Probe')
        self.Append(probe_container_item)
        
        # Print html structure of comment window
        probe_xml_item = wx.MenuItem(self, id=ID_PROBE_XML, text='Print HTML')
        self.Append(probe_xml_item)
        
        print(ID_PROBE_CONTAINER)
        print(ID_PROBE_XML)
        
        