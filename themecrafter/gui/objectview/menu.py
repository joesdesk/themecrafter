import wx

from .treectrl import Frame as ObjectViewFrame

ID_VIEW_OBJECTS = 20


class Menu(wx.Menu):
    
    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        
        # Set menu items
        view_objects = self.Append(ID_VIEW_OBJECTS, "View Objects")
        
        # Frame associated with menu
        self.objviewframe = ObjectViewFrame(None, id=wx.ID_ANY, title='ObjectView')
        
        self.Bind(wx.EVT_MENU, self.test_call, id=ID_VIEW_OBJECTS)
        
        
        
    def test_call(self, evt):
        event_id = evt.GetId()
        
        self.objviewframe.Show()