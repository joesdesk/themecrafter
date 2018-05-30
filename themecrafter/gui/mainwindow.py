import wx

from .mainwidgets.mainmenu import MainMenuBar

from .mainwidgets.mainsplitter import MainWindowSplitter
from .commentwindow import CommentWindow
from .elementlist.tokenlist import TokenListCtrl

from ..output.session import ThemeCrafterSession

from . import EVT_DATA_LOAD

# https://wxpython.org/Phoenix/docs/html/events_overview.html#custom-event-summary
# event propagation http://zetcode.com/wxpython/events/

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
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, size=(800,600))

        # Create a new session with the winddow to interact with package routines

        # Add a main menu
        main_menubar = MainMenuBar()
        self.SetMenuBar(main_menubar)

            # See https://wiki.wxpython.org/self.Bind%20vs.%20self.button.Bind
        #self.Bind(wx.EVT_MENU, self.data_loaded, main_menubar)
        self.Bind(EVT_DATA_LOAD, self.data_loaded)
        
        # Add splitters to obtain 4 panels on which to add widgets.
        main_splitter = MainWindowSplitter(self)
        LT_panel = main_splitter.LT_panel
        LB_panel = main_splitter.LB_panel
        RT_panel = main_splitter.RT_panel
        RB_panel = main_splitter.RB_panel

        # Add widget to read comments
        RT_sizer = wx.BoxSizer(wx.VERTICAL)

        self.comment_reader = CommentWindow(RT_panel, "aweg")
        #comment_reader = wx.TextCtrl(RT_panel)

        #comment_reader = wx.html.HtmlWindow(RT_panel)
        #comment_reader.SetPage("<html>awefawef</html>")

        RT_sizer.Add(self.comment_reader, proportion=1, flag=wx.EXPAND|wx.ALL)
        RT_panel.SetSizer(RT_sizer)


        # Add widget to tabulate cells
        LB_sizer = wx.BoxSizer(wx.VERTICAL)

        # List of vocabulary, tokens and n-grams
        notebook = wx.Notebook(LB_panel)
        
        self.token_list_ctrl = TokenListCtrl(notebook)
        
        notebook.AddPage(self.token_list_ctrl, 'Tokens')
        
        LB_sizer.Add(notebook, proportion=1, flag=wx.EXPAND|wx.ALL)
        LB_panel.SetSizer(LB_sizer)

		
    def data_loaded(self, evt):
        data = evt.attr
        session = ThemeCrafterSession(data)
        
        #text = session.as_html_text()
        #self.comment_reader.SetPage(text)
        
        #tokens = session.get_token_list()
        tokens = []
        for i in range(10):
            tokens.append(str((5,3)))
        self.token_list_ctrl.set_data(tokens)
		