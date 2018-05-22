import wx

class MainWindowSplitter(wx.SplitterWindow):

    def __init__(self, parent, style=wx.SP_3D):
        '''Initializes the main '''
        wx.SplitterWindow.__init__(self, parent=parent, style=style)
        self.SetSashGravity(0.5)

        # Add a top-bottom splitter on the left panel
        left_splitter = wx.SplitterWindow(parent=self, style=style)
        left_splitter.SetSashGravity(0.5)

        self.LT_panel = wx.Panel(left_splitter)
        self.LB_panel = wx.Panel(left_splitter)
        left_splitter.SplitHorizontally(self.LT_panel, self.LB_panel)

        # Add a top-bottom splitter on the right panel
        right_splitter = wx.SplitterWindow(parent=self, style=style)
        right_splitter.SetSashGravity(0.5)

        self.RT_panel = wx.Panel(right_splitter)
        self.RB_panel = wx.Panel(right_splitter)
        right_splitter.SplitHorizontally(self.RT_panel, self.RB_panel)

        # Having set up the secondary sizers, perform the split
        self.SplitVertically(left_splitter, right_splitter)


#ex = wx.App()
#Mywin(None,'Splitter Demo')
#ex.MainLoop()
