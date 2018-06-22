# Module that handles preprocessing events

import wx
import wx.lib.newevent

ID_XML_LOAD = 85
ID_XML_SAVE = 86

ID_NLP_PARSE = 87
ID_SEL_FEAT = 88

OnXMLLoad, EVT_XML_LOAD = wx.lib.newevent.NewCommandEvent()
OnXMLSave, EVT_XML_SAVE = wx.lib.newevent.NewCommandEvent()

OnNLPParse, EVT_NLP_PARSE = wx.lib.newevent.NewCommandEvent()
OnSelFeat, EVT_SEL_FEAT = wx.lib.newevent.NewCommandEvent()

    
class PreprocessingMenu(wx.Menu):
    
    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        
        # Set menu items
        item_loadxml = self.Append(ID_XML_LOAD, "Load XML")
        item_savexml = self.Append(ID_XML_SAVE, "Save XML")
        
        self.AppendSeparator()
        
        item_nlpparse = self.Append(ID_NLP_PARSE, "NLP")
        item_featsel = self.Append(ID_SEL_FEAT, "Feature Selection")
        
        self.Bind(wx.EVT_MENU, self.test_call)
        
    def test_call(self, evt):
        event_id = evt.GetId()
        
        if event_id==ID_XML_LOAD:
            filename = ""
            newevent = OnXMLLoad(xml_filename=filename, \
                id=ID_XML_LOAD)
            
        elif event_id==ID_XML_SAVE:
            newevent = OnXMLSave(id=ID_XML_SAVE)
            
        elif event_id==ID_NLP_PARSE:
            newevent = OnNLPParse(id=ID_NLP_PARSE)
            
        elif event_id==ID_SEL_FEAT:
            newevent = OnSelFeat(id=ID_SEL_FEAT)
        
        else:
            newevent = None
            
        if newevent is not None:
            wx.PostEvent(self.parent, newevent)
            
            