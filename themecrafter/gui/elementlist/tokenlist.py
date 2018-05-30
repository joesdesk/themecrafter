#http://zetcode.com/wxpython/advanced/
#http://www.blog.pythonlibrary.org/2011/01/04/wxpython-wx-listctrl-tips-and-tricks/
#http://nullege.com/codes/show/src%40p%40a%40paimei-HEAD%40console%40modules%40_PAIMEIpstalker%40HitsListCtrl.py/30/wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin/python

import wx
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin


class TokenListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):

    def __init__(self, parent):
        ''''''
        # Initialize list control with column widths that fills parent
        wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)

        # Pre-set columns
        self.InsertColumn(0, 'token', width=140)
        self.InsertColumn(1, 'synonyms', width=130)
        self.InsertColumn(2, 'counts', width=90)

        #

    def set_data(self, data):
        '''Sets the data in the list control.'''
        idx = 0
        for i in data:
            index = self.InsertItem(idx, i[0])
            self.SetItem(index, 1, i[1])
            self.SetItem(index, 2, i[2])
            idx += 1
