import wx

from .mainwidgets.mainmenu import MainMenuBar
from .mainwidgets.mainsplitter import MainWindowSplitter
from .mainwidgets.commentreader import MyHtmlFrame

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

        # Add widget to read comments
        RT_sizer = wx.BoxSizer(wx.VERTICAL)

        comment_reader = MyHtmlFrame(RT_panel, "aweg")
        #comment_reader = wx.TextCtrl(RT_panel)

        #comment_reader = wx.html.HtmlWindow(RT_panel)
        #comment_reader.SetPage("<html>awefawef</html>")

        RT_sizer.Add(comment_reader, proportion=1, flag=wx.EXPAND|wx.ALL)
        RT_panel.SetSizer(RT_sizer)
