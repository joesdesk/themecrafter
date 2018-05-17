import wx

from gui.mainwidgets.mainmenu import MainMenuBar
from gui.mainwidgets.mainsplitter import MainWindowSplitter

class MainWindow(wx.Frame):
    '''
    This window is the one containing the main controls and panels
    of the program.
    '''

    def __init__(self, parent, title=""):
        '''
        Initializes the main window.
        '''

        # Since we will use a toolbar, we use the wx.Frame
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title)

        # Add a main menu
        main_menubar = MainMenuBar()
        self.SetMenuBar(main_menubar)

        # Add splitters to obtain 4 panels on which to add widgets.
        main_splitter = MainWindowSplitter(self)
        LT_panel = main_splitter.LT_panel
        LB_panel = main_splitter.LB_panel
        RT_panel = main_splitter.RT_panel
        RB_panel = main_splitter.RB_panel

        # Add a secondary top-bottom splitter to
        # the left and right panes
