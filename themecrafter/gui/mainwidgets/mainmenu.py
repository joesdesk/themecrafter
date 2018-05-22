import wx

# Custom event ids: http://zetcode.com/wxpython/events/
#ID_MENU_NEW = wx.NewId()
#ID_MENU_OPEN = wx.NewId()
#ID_MENU_SAVE = wx.NewId()

class MainMenuBar(wx.MenuBar):
    """Class to hold the top menus (file, edit, etc.)"""

    def __init__(self, session):
        """"""

        # Create a menu bar
        wx.MenuBar.__init__(self)

        # Get session
        self.session = session

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
        load_csv = datamenu.Append(wx.ID_ANY, "Load CSV")
        self.Append(datamenu, "Data")

        # Test button functionality
        self.Bind(wx.EVT_MENU, self.load_data, load_csv)


    def load_data(self, menu_evt):
        print("LOAD_CSV")
