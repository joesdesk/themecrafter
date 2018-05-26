# This class defines global events associated with different
# interactions with the session, which is the package interface.
# See: https://wiki.wxpython.org/CustomEventClasses

import wx.lib.newevent

ID_DATA_LOADED = 50


OnDataLoad, EVT_DATA_LOAD = wx.lib.newevent.NewCommandEvent()
#SomeNewCommandEvent, EVT_SOME_NEW_COMMAND_EVENT = wx.lib.newevent.NewCommandEvent()


#class SessionEventHandler:

#    def __init_