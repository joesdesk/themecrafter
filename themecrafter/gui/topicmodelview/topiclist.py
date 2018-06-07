# wxPython: wx.ListCtrl Tips and Tricks
# http://www.blog.pythonlibrary.org/2011/01/04/wxpython-wx-listctrl-tips-and-tricks/

import wx
 
########################################################################
class Car(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, make, model, year, color="Blue"):
        """Constructor"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
 
########################################################################
class TopicList(wx.ListCtrl):
    
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)
        
        
    def set_data(self, df):
        '''Sets the data, a list of tuples, in the list control.'''
        
        # Empty contents
        self.clear()
        
        # Pre-set columns
        nrows, ncols = df.shape
        columns = df.columns.values.tolist()
        self.set_columns(columns)
        
        # Set data
        df_data = df.astype(str).values.tolist()
        for j, row in enumerate(df_data):
            self.InsertItem(j, '')
            for i, col in enumerate(row):
                self.SetItem(j, i, col)

 
########################################################################
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 
        rows = [Car("Ford", "Taurus", "1996"),
                Car("Nissan", "370Z", "2010"),
                Car("Porche", "911", "2009", "Red")
                ]
 
        self.list_ctrl = TopicList(self)
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.list_ctrl.InsertColumn(0, "Make")
        self.list_ctrl.InsertColumn(1, "Model")
        self.list_ctrl.InsertColumn(2, "Year")
        self.list_ctrl.InsertColumn(3, "Color")
 
        index = 0
        self.myRowDict = {}
        for row in rows:
            self.list_ctrl.InsertItem(index, row.make)
            self.list_ctrl.SetItem(index, 1, row.model)
            self.list_ctrl.SetItem(index, 2, row.year)
            self.list_ctrl.SetItem(index, 3, row.color)
            self.myRowDict[index] = row
            index += 1
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onItemSelected(self, event):
        """"""
        index = event.GetIndex()
        event.Skip()
 
########################################################################
class MyFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "List Control Tutorial")
        panel = MyPanel(self)
        self.Show()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()