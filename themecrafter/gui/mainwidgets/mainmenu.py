import wx

from ..dataloading.datamenu import DataMenu

# Custom event ids: http://zetcode.com/wxpython/events/
#ID_MENU_NEW = wx.NewId()
#ID_MENU_OPEN = wx.NewId()
#ID_MENU_SAVE = wx.NewId()


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

        # Menu for data loading
        datamenu = DataMenu(self)
        self.Append(datamenu, "Data")
        
        