import wx

class MainWindowSplitter(wx.SplitterWindow):

    def __init__(self, parent, style=wx.SP_3D):
        '''Initializes the main '''
        wx.SplitterWindow.__init__(self, parent=parent, style=style)
        self.SetSashGravity(0.5)

        # Add a top-bottom splitter on the left panel
        left_splitter = wx.SplitterWindow(parent=self, style=style)
        left_splitter.SetSashGravity(0.5)

        self.panel_LT = wx.Panel(left_splitter)
        self.panel_LB = wx.Panel(left_splitter)
        left_splitter.SplitHorizontally(self.panel_LT, self.panel_LB)

        # Add a top-bottom splitter on the right panel
        right_splitter = wx.SplitterWindow(parent=self, style=style)
        right_splitter.SetSashGravity(0.5)

        self.panel_RT = wx.Panel(right_splitter)
        self.panel_RB = wx.Panel(right_splitter)
        right_splitter.SplitHorizontally(self.panel_RT, self.panel_RB)

        # Having set up the secondary sizers, perform the split
        self.SplitVertically(left_splitter, right_splitter)


#ex = wx.App()
#Mywin(None,'Splitter Demo')
#ex.MainLoop()
