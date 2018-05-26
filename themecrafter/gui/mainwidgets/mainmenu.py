import wx

from ..dataloading import CsvDialog
from ..dataloading.events import OnDataLoad, EVT_DATA_LOAD

# Custom event ids: http://zetcode.com/wxpython/events/
#ID_MENU_NEW = wx.NewId()
#ID_MENU_OPEN = wx.NewId()
#ID_MENU_SAVE = wx.NewId()

ID_LOAD_DATA_CSV = 50


class MainMenuBar(wx.MenuBar):
    """Class to hold the top menus (file, edit, etc.)"""

    def __init__(self):
        """"""

        # Create a menu bar
        wx.MenuBar.__init__(self)

        # Test to see if initialized
        print("main menu initialized")

        # Menu for the application and user files
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program.")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program.")
        self.Append(filemenu, "File")

        # Menu for the editing process
        editmenu = wx.Menu()
        editmenu.Append(wx.ID_ANY, "Undo")
        editmenu.Append(wx.ID_ANY, "Redo")
        self.Append(editmenu, "Edit")

        # Menu for the data loading process
        datamenu = wx.Menu()
        datamenu.Append(ID_LOAD_DATA_CSV, "Import CSV")
        #datamenu.AppendSeparator()
        #datamenu.Append(ID_LOAD_DATA_PRESET1, "Load Twenty News Groups")
        #datamenu.Append(ID_LOAD_DATA_PRESET2, "Load BG Survey")
        #datamenu.Append(ID_LOAD_DATA_PRESET3, "Load Grad Reports")
        #datamenu.Append(ID_LOAD_DATA_PRESET4, "Load Students Review")
        self.Append(datamenu, "Data")

        # Test button functionality
        self.Bind(wx.EVT_MENU, self.load_csv_data, id=ID_LOAD_DATA_CSV)
        self.Bind(EVT_DATA_LOAD, self.print_confirm)
        #self.Bind(wx.EVT_MENU, self.load_preset_data, id=ID_LOAD_DATA_PRESET1)
        #self.Bind(wx.EVT_MENU, self.load_preset_data, id=ID_LOAD_DATA_PRESET2)
        #self.Bind(wx.EVT_MENU, self.load_preset_data, id=ID_LOAD_DATA_PRESET3)
        #self.Bind(wx.EVT_MENU, self.load_preset_data, id=ID_LOAD_DATA_PRESET4)

    
    def load_csv_data(self, e):
        """"""
        #id = e.GetId()
        #print(id)
        
        # Ask the user to open file
        # https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
        with CsvDialog(self) as csv_dialog:

            exit_status = csv_dialog.ShowModal()
            
            #if exit_status==wx.ID_CANCEL:
                # The user changed their mind
                # See https://wxpython.org/Phoenix/docs/html/wx.Dialog.html
            #    return None

            # Proceed loading the file chosen by the user
            #data = csv_dialog.extract_data()
            #self.data = data
    
    def print_confirm(self, e):
        print("aefawe")
        e.Skip()
        
    #def load_preset_data(self, e):
        #""""""
        #id = e.GetId()
        #if id==ID_LOAD_DATA_PRESET1:
        #    #self.session.load_preset_data('NewsGroups')
        #print(k)
        #e.Skip()
        #evt = OnDataLoad(attr1="hello")
        #wx.PostEvent(self.GetParent(), evt)
        #pass
        
        
        
		