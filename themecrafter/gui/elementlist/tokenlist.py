#http://zetcode.com/wxpython/advanced/
#http://www.blog.pythonlibrary.org/2011/01/04/wxpython-wx-listctrl-tips-and-tricks/
#http://nullege.com/codes/show/src%40p%40a%40paimei-HEAD%40console%40modules%40_PAIMEIpstalker%40HitsListCtrl.py/30/wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin/python

from pandas import DataFrame

import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin


class TokenListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):

    def __init__(self, parent):
        ''''''
        # Initialize list control with column widths that fills parent
        wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)
    
    def clear(self):
        '''Reset the list control.'''
        self.DeleteAllItems()
        self.DeleteAllColumns()
    
    def set_columns(self, columns):
        '''Set columns in the list control.'''
        for i, colname in enumerate(columns):
            self.InsertColumn(i, colname, width=90)
    

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
                