import wx

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

        # Menu for the data loading process
        datamenu = wx.Menu()
        load_csv = datamenu.Append(wx.ID_ANY, "Load CSV")
        datamenu.AppendSeparator()
        load_newsgroups_data = datamenu.Append(wx.ID_ANY, "Load News Groups")
        load_bg_survey_data = datamenu.Append(wx.ID_ANY, "Load BG Survey")
        load_grad_reports = datamenu.Append(wx.ID_ANY, "Load Grad Reports")
        load_students_rev_data = datamenu.Append(wx.ID_ANY, "Load Students Review")
        self.Append(datamenu, "Data")

        # Test button functionality
        self.Bind(wx.EVT_MENU, self.load_preset_data, load_csv)
		
        self.Bind(wx.EVT_MENU, self.load_preset_data, load_newsgroups_data)
        self.Bind(wx.EVT_MENU, self.load_preset_data, load_bg_survey_data)
        self.Bind(wx.EVT_MENU, self.load_preset_data, load_grad_reports)
        self.Bind(wx.EVT_MENU, self.load_preset_data, load_students_rev_data)


    def load_preset_data(self, menu_evt):
        #self.session.load_preset_data('NewsGroups')
        #print(k)
        menu_evt.Skip()
        #evt = OnDataLoad(attr1="hello")
        #wx.PostEvent(wx.Window, evt)
		
		