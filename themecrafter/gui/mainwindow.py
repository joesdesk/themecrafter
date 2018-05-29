import wx

from .mainwidgets.mainmenu import MainMenuBar

from .mainwidgets.mainsplitter import MainWindowSplitter
from .commentwindow import CommentWindow
from .mainwidgets.tokenlist import TokenListCtrl

from ..interface.session import ThemeCrafterSession

from .dataloading.events import EVT_DATA_LOAD, \
    ID_DATA_LOAD_NEWSGROUPS, ID_DATA_LOAD_BGSURVEY, \
    ID_DATA_LOAD_GRADREPORTS, ID_DATA_LOAD_STUDENTSREVIEWS

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
        self.session = ThemeCrafterSession()

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

        #word_reader = MySheet(LB_panel)
        token_list = TokenListCtrl(LB_panel)

        LB_sizer.Add(token_list, proportion=1, flag=wx.EXPAND|wx.ALL)
        LB_panel.SetSizer(LB_sizer)

		
    def data_loaded(self, evt):
        print('Event reached main window.')
        
        data = evt.attr
        id = evt.GetId()
        
        if data is not None:
            self.session.load_data(data=data)
            id = -1
            
        if id==ID_DATA_LOAD_NEWSGROUPS:
            self.session.load_preset_data(data='NewsGroups')
        elif id==ID_DATA_LOAD_BGSURVEY:
            self.session.load_preset_data(data='BGSurvey')
        elif id==ID_DATA_LOAD_GRADREPORTS:
            self.session.load_preset_data(data='GradReports')
        elif id==ID_DATA_LOAD_STUDENTSREVIEWS:
            self.session.load_preset_data(data='StudentsReview')

        text = self.session.to_html_text()
        self.comment_reader.SetPage(text)
		
		