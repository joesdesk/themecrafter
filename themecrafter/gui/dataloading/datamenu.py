# Menu entry for data loading that can call a dialog to
# select text data from a CSV

import wx
import wx.lib.newevent

import pandas as pd

from .csvdialog import CsvDialog


# Command events can be propagated up the parent heirarchy through e.Skip()
ID_DATALOAD_CSV = 50

# This class defines global events associated with different
# interactions with the session, which is the package interface.
# See: https://wiki.wxpython.org/CustomEventClasses

OnDataLoad, EVT_DATA_LOAD = wx.lib.newevent.NewCommandEvent()


class DataMenu(wx.Menu):

    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        
        # Add load csv data entry
        self.Append(id=ID_DATALOAD_CSV, item="Import CSV")
        
        # Attach events to menu's entries
        self.Bind(wx.EVT_MENU, self.load_csv_data, id=ID_DATALOAD_CSV)
        
        
    def load_csv_data(self, event):
        """"""
        # Ask the user to open file
        # https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
        with CsvDialog() as csv_dialog:
            exit_status = csv_dialog.ShowModal()
            if exit_status==wx.ID_CANCEL:
                # The user changed their mind
                # See https://wxpython.org/Phoenix/docs/html/wx.Dialog.html
                return None

        series = pd.read_csv(csv_dialog.filename, sep=',', \
            header=csv_dialog.header_line_num, \
            usecols=[csv_dialog.header_label], squeeze=True)
        data = series.tolist()
        
        evt = OnDataLoad(attr=data, id=ID_DATALOAD_CSV)
        wx.PostEvent(self.parent, evt)
        
        