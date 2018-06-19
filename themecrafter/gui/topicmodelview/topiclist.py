# wxPython: wx.ListCtrl Tips and Tricks
# http://www.blog.pythonlibrary.org/2011/01/04/wxpython-wx-listctrl-tips-and-tricks/

import wx
import pandas as pd


class TopicListCtrl(wx.ListCtrl):
    
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
    
    def clear(self):
        '''Reset the list control.'''
        self.DeleteAllItems()
        self.DeleteAllColumns()
        
    def set_columns(self, columns):
        '''Set columns in the list control.'''
        for i, colname in enumerate(columns):
            self.InsertColumn(i, colname, width=100)
 
########################################################################
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        
        self.list_ctrl = TopicListCtrl(self)
        
        # Create data frame to test
        data = [("Ford", "Taurus", "1996"),
                ("Nissan", "370Z", "2010"),
                ("Porche", "911", "2009", "Red")]
       
        df = pd.DataFrame(data, columns=["Make", "Model", "Year", "Color"])
        
        self.list_ctrl.set_data(df)
        
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        
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