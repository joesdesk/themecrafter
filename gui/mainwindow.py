import wx

from gui.mainwidgets.mainmenu import MainMenuBar

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
        mainmenubar = MainMenuBar()
        #self.SetMenuBar(mainmenubar)
