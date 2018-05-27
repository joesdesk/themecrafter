# Menu entry for data loading that can call a dialog to
# select text data from a CSV

import wx

from . import CsvDialog
from .events import OnDataLoad, ID_DATA_LOADED
from .events import ID_DATA_LOAD_NEWSGROUPS, ID_DATA_LOAD_BGSURVEY
from .events import ID_DATA_LOAD_GRADREPORTS, ID_DATA_LOAD_STUDENTSREVIEWS


class DataMenu(wx.Menu):

    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        #self.SetParent(parent)
        
        # Add load csv data entry
        self.Append(id=ID_DATA_LOADED, item="Import CSV")
        self.AppendSeparator()

        # Add submenu for preset data
        preset_menu = wx.Menu()
        preset_menu.Append(id=ID_DATA_LOAD_NEWSGROUPS, item="Twenty News Groups")
        preset_menu.Append(id=ID_DATA_LOAD_BGSURVEY, item="BG Survey")
        preset_menu.Append(id=ID_DATA_LOAD_GRADREPORTS, item="Grad Reports")
        preset_menu.Append(id=ID_DATA_LOAD_STUDENTSREVIEWS, item="Students Review")
        self.AppendSubMenu(submenu=preset_menu, text='Import Preset')
        
        # Attach events to menu's entries
        self.Bind(wx.EVT_MENU, self.load_csv_data, id=ID_DATA_LOADED)
        preset_menu.Bind(wx.EVT_MENU, self.load_preset_data)
        
        
    def load_csv_data(self, event):
        """"""
        #id = e.GetId()
        #print(id)
        #parent = self.GetParent()
        # Ask the user to open file
        # https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
        with CsvDialog() as csv_dialog:

            exit_status = csv_dialog.ShowModal()
            
            #if exit_status==wx.ID_CANCEL:
                # The user changed their mind
                # See https://wxpython.org/Phoenix/docs/html/wx.Dialog.html
            #    return None

            # Proceed loading the file chosen by the user
            #data = csv_dialog.extract_data()
            #self.data = data
            #print(csv_dialog.data)
            #print(csv_dialog.data)
            evt = OnDataLoad(attr=csv_dialog.data, id=ID_DATA_LOADED)
            wx.PostEvent(self.parent, evt)
        
        
    def load_preset_data(self, event):
        '''Event handler for "load preset data" events from submenus.'''
        #event.Skip()
        id = event.GetId()
        #print(id)
        #if id==ID_LOAD_DATA_PRESET1:
        #    #self.session.load_preset_data('NewsGroups')
        #print(k)
        #e.Skip()
        evt = OnDataLoad(attr="hello", id=id)
        wx.PostEvent(self.parent, evt)
        #pass