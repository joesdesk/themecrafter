import wx

class MainMenuBar(wx.MenuBar):
    """Class to hold the top menus (file, edit, etc.)"""

    def __init__(self):
        """"""

        # Create a menu bar
        wx.MenuBar.__init__(self)

        # Test to see if initialized
        print("main menu initialized")

        # Menu for handling files
        filemenu = wx.Menu()
        self.Append(filemenu, "File")
