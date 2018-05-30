# Menu entry for data loading that can call a dialog to
# select text data from a CSV

import wx

import pandas as pd

from ...datasets import NewsGroupsDataSet, BGSurveyDataSet, \
    GradReportsDataSet, StudentsReviewDataSet

from . import CsvDialog

import wx.lib.newevent

# Command events can be propagated up the parent heirarchy through e.Skip()
ID_DATA_LOADED = 50

ID_DATA_LOAD_NEWSGROUPS = 55
ID_DATA_LOAD_BGSURVEY = 56
ID_DATA_LOAD_GRADREPORTS = 57
ID_DATA_LOAD_STUDENTSREVIEWS = 58

# This class defines global events associated with different
# interactions with the session, which is the package interface.
# See: https://wiki.wxpython.org/CustomEventClasses

OnDataLoad, EVT_DATA_LOAD = wx.lib.newevent.NewCommandEvent()


class DataMenu(wx.Menu):

    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        
        # Add load csv data entry
        self.Append(id=ID_DATA_LOADED, item="Import CSV")
        self.AppendSeparator()

        # Add submenu for preset data
        preset_menu = wx.Menu()
        preset_menu.Append(id=ID_DATA_LOAD_NEWSGROUPS, item="Twenty News Groups")
        preset_menu.Append(id=ID_DATA_LOAD_BGSURVEY, item="BG Survey")
        preset_menu.Append(id=ID_DATA_LOAD_GRADREPORTS, item="Grad Reports")
        preset_menu.Append(id=ID_DATA_LOAD_STUDENTSREVIEWS, item="Students Review")
        self.AppendSubMenu(submenu=preset_menu, text='Import Preset')
        
        # Attach events to menu's entries
        self.Bind(wx.EVT_MENU, self.load_csv_data, id=ID_DATA_LOADED)
        preset_menu.Bind(wx.EVT_MENU, self.load_preset_data)
        
        
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
        
        evt = OnDataLoad(attr=data, id=ID_DATA_LOADED)
        wx.PostEvent(self.parent, evt)
        
        
    def load_preset_data(self, event):
        '''Event handler for "load preset data" events from submenus.'''
        id = event.GetId()
        
        if id==ID_DATA_LOAD_NEWSGROUPS:
            data = NewsGroupsDataSet()
        elif id==ID_DATA_LOAD_BGSURVEY:
            data = BGSurveyDataSet()
        elif id==ID_DATA_LOAD_GRADREPORTS:
            data = GradReportsDataSet()
        elif id==ID_DATA_LOAD_STUDENTSREVIEWS:
            data = StudentsReviewDataSet()
        else:
            data = []
        
        evt = OnDataLoad(attr=data.X, id=id)
        wx.PostEvent(self.parent, evt)

        