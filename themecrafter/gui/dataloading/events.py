# This class defines global events associated with different
# interactions with the session, which is the package interface.
# See: https://wiki.wxpython.org/CustomEventClasses

import wx.lib.newevent

# Command events can be propagated up the parent heirarchy through e.Skip()
ID_DATA_LOADED = 50

ID_DATA_LOAD_NEWSGROUPS = 55
ID_DATA_LOAD_BGSURVEY = 56
ID_DATA_LOAD_GRADREPORTS = 57
ID_DATA_LOAD_STUDENTSREVIEWS = 58

OnDataLoad, EVT_DATA_LOAD = wx.lib.newevent.NewCommandEvent()




#class SessionEventHandler:

#    def __init_